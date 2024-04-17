rule Rename:
    input: "./Files"
    output: "./output"
    shell: "mv {input} {output}"