const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType,
  Header, Footer, PageNumber, PageBreak,
} = require("docx");

const NOTES = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const OUT = process.argv[3];

const DARK = "13453B";
const GOLD = "A8762A";
const MUTED = "6E7D78";
const RULE = "D9E2DE";

const HEAD = "Cambria";
const BODY = "Calibri";

function rule(before = 0, after = 0) {
  return new Paragraph({
    spacing: { before, after },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 1 } },
    children: [],
  });
}

const children = [];

// ---------- heading ----------
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [new TextRun({
    text: "SPEAKER NOTES", font: BODY, size: 17, bold: true,
    color: GOLD, characterSpacing: 60,
  })],
}));
children.push(new Paragraph({
  spacing: { after: 100 },
  children: [new TextRun({
    text: "Managing Financial Performance Across Repairs & Maintenance",
    font: HEAD, size: 40, bold: true, color: DARK,
  })],
}));
children.push(new Paragraph({
  spacing: { after: 220 },
  children: [new TextRun({
    text: "Sandra Vermaak   ·   Codi Group   ·   Finance Business Partner interview",
    font: BODY, size: 20, color: MUTED,
  })],
}));

// ---------- timing summary ----------
const rows = [new TableRow({
  tableHeader: true,
  children: ["Slide", "Runs", "Elapsed", ""].map((h, i) => new TableCell({
    width: { size: [900, 1100, 1300, 6060][i], type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: "F1F5F3" },
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ children: [new TextRun({
      text: h, font: BODY, size: 15, bold: true, color: MUTED, characterSpacing: 30,
    })] })],
  })),
})];

for (const n of NOTES) {
  const parts = (n.cue || "").split("·").map(s => s.trim());
  rows.push(new TableRow({
    children: [
      String(n.slide),
      parts[0] || "",
      (parts[1] || "").replace(" elapsed", ""),
      n.slide === 1 ? "Title slide" : n.title,
    ].map((t, i) => new TableCell({
      width: { size: [900, 1100, 1300, 6060][i], type: WidthType.DXA },
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [new Paragraph({ children: [new TextRun({
        text: t, font: BODY, size: 19,
        bold: i === 0, color: i === 3 ? "33423D" : (i === 0 ? DARK : MUTED),
      })] })],
    })),
  }));
}

children.push(new Table({
  columnWidths: [900, 1100, 1300, 6060],
  width: { size: 9360, type: WidthType.DXA },
  borders: {
    top: { style: BorderStyle.SINGLE, size: 4, color: RULE },
    bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: RULE },
    insideVertical: { style: BorderStyle.NONE },
  },
  rows,
}));

children.push(new Paragraph({
  spacing: { before: 160, after: 0 },
  children: [new TextRun({
    text: "Total 1,328 words — about 9 minutes 40 at a normal speaking pace, "
        + "10 minutes 40 if you slow down. The timings are a guide, not a script.",
    font: BODY, size: 18, italics: true, color: MUTED,
  })],
}));

// ---------- the notes ----------
NOTES.forEach((n, idx) => {
  children.push(new Paragraph({
    pageBreakBefore: true,
    spacing: { after: 40 },
    children: [new TextRun({
      text: `SLIDE ${n.slide}`,
      font: BODY, size: 16, bold: true, color: GOLD, characterSpacing: 60,
    })],
  }));

  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { after: 40 },
    children: [new TextRun({
      text: n.slide === 1 ? "Title slide" : n.title,
      font: HEAD, size: 30, bold: true, color: DARK,
    })],
  }));

  children.push(new Paragraph({
    spacing: { after: 40 },
    children: [new TextRun({
      text: n.cue, font: BODY, size: 18, color: MUTED,
    })],
  }));

  children.push(rule(60, 160));

  for (const p of n.paragraphs) {
    const isAside = p.startsWith("[Note]");
    children.push(new Paragraph({
      spacing: { after: 180, line: 300 },
      children: [new TextRun({
        text: isAside ? p.replace(/^\[Note\]\s*/, "") : p,
        font: BODY, size: 23,
        italics: isAside,
        color: isAside ? MUTED : "1F2A27",
      })],
    }));
  }
});

const doc = new Document({
  creator: "Sandra Vermaak",
  title: "Speaker notes — Managing Financial Performance Across Repairs & Maintenance",
  description: "",
  styles: {
    default: {
      document: { run: { font: BODY, size: 23, color: "1F2A27" } },
      heading1: { run: { font: HEAD, size: 30, bold: true, color: DARK } },
    },
  },
  sections: [{
    properties: { page: { margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({
            children: ["Speaker notes   ·   Sandra Vermaak   ·   page ", PageNumber.CURRENT],
            font: BODY, size: 16, color: MUTED,
          })],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(OUT, b);
  console.log("written:", OUT, `(${b.length} bytes)`);
});
