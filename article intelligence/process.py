#!/usr/bin/env python3
# merge_md.py
"""
将当前目录下除 all.md 之外的所有 .md 文件内容合并到 all.md。
不会递归子目录；如需递归可把 Path.glob("*.md") 改成 rglob("*.md")。
"""

from pathlib import Path

def main() -> None:
    out_path = Path("all.md")            # 输出文件
    # —— 关键逻辑：排除 all.md 自身 ——
    md_files = sorted(
        p for p in Path(".").glob("*.md") if p.name != out_path.name
    )

    with out_path.open("w", encoding="utf-8") as out_fp:
        for idx, md in enumerate(md_files, 1):
            out_fp.write(f"\n\n<!-- ========== {idx}. {md.name} ========== -->\n\n")
            out_fp.write(md.read_text(encoding="utf-8"))

    print(f"已写入 {out_path}，合并 {len(md_files)} 个 .md 文件。")

if __name__ == "__main__":
    main()
