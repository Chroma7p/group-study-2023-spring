rule shebang {
    strings:
        $shebang = /^#!(\/[^\/ ]*)+\/?/
    condition:
        $shebang
}
rule maybe_python_executable {
    strings:
        $ident = /python(2|3)\r*\n/
    condition:
        shebang and $ident
}

rule flag {
    strings:
        $ctf4b = "ctf4b{"
    condition:
        $ctf4b at 0
}

rule aa {
    strings:
        $aa = "aa"
    condition:
        $aa
}

