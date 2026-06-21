import { copyFileSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const output = resolve(root, "dist");

rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
copyFileSync(resolve(root, "index.html"), resolve(output, "index.html"));

if (existsSync(resolve(root, ".nojekyll"))) {
  copyFileSync(resolve(root, ".nojekyll"), resolve(output, ".nojekyll"));
}

console.log("静态页面已生成到 dist/");
