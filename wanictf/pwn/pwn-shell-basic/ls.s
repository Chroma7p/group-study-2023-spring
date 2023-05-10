section .data
    dir db "/usr/bin/",0
    args db "-la",0

section .text
    global _start

_start:
    ; ファイルディスクリプタ0（標準入力）を閉じる
    mov eax, 6          ; sys_closeのシステムコール番号は6
    xor ebx, ebx        ; ファイルディスクリプタ0を示すebxを0に設定
    int 0x80            ; システムコールを呼び出す

    ; "/usr/bin/"をカレントディレクトリに設定するchdirシステムコールを呼び出す
    mov eax, 0x0f       ; sys_chdirのシステムコール番号は15
    mov ebx, dir        ; ディレクトリのパスをebxにロード
    int 0x80            ; システムコールを呼び出す

    ; "ls -la"を実行するexecveシステムコールを呼び出す
    mov eax, 0xb        ; sys_execveのシステムコール番号は11
    mov ebx, args       ; 引数の文字列をebxにロード
    xor ecx, ecx        ; 環境変数のポインタはNULLに設定
    push ecx            ; 引数の終端NULLをプッシュ
    mov ecx, esp        ; 引数配列の先頭アドレスをecxに設定
    int 0x80            ; システムコールを呼び出す

    ; システムコールの戻り値を終了ステータスとして使用する
    mov eax, ebx        ; execveの戻り値をeaxにコピー
    xor ebx, ebx        ; ステータスコードは0に設定
    mov eax, 1          ; sys_exitのシステムコール番号は1
    int 0x80            ; システムコールを呼び出す
