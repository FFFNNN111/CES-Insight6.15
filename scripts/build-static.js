const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const dist = path.join(root, "dist");

const entries = [
  "index.html",
  ".nojekyll",
  "README.md",
  path.join("启动项", "CES情感分析.html"),
  path.join("启动项", "ces_browser_dataset.js"),
];

function copyFile(relativePath) {
  const from = path.join(root, relativePath);
  const to = path.join(dist, relativePath);
  if (!fs.existsSync(from)) {
    throw new Error(`Missing required file: ${relativePath}`);
  }
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.copyFileSync(from, to);
}

fs.rmSync(dist, { recursive: true, force: true });
for (const entry of entries) {
  copyFile(entry);
}

console.log(`Static build completed: ${dist}`);
