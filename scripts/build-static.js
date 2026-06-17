// Cloudflare Pages build script
// Copies CES情感分析.html to dist/ for deployment

var fs = require("fs");
var path = require("path");

var distDir = path.join(__dirname, "..", "dist");
var srcDir = path.join(__dirname, "..");

// Ensure dist directory exists
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
}

// Required files: [source (relative to repo root), dest (relative to dist/)]
var files = [
  ["CES情感分析.html", "index.html"],
];

files.forEach(function (pair) {
  var src = path.join(srcDir, pair[0]);
  var dest = path.join(distDir, pair[1]);
  if (!fs.existsSync(src)) {
    console.error("Missing required file: " + pair[0]);
    process.exit(1);
  }
  var destParent = path.dirname(dest);
  if (!fs.existsSync(destParent)) {
    fs.mkdirSync(destParent, { recursive: true });
  }
  fs.copyFileSync(src, dest);
  console.log("Copied: " + pair[0] + " -> dist/" + pair[1]);
});

console.log("Build complete.");