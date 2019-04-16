  1           0 LOAD_CONST               0 ('\x1b[0m')
              2 STORE_NAME               0 (N)

  2           4 LOAD_CONST               1 ('\x1b[1;37m\x1b[31m')
              6 STORE_NAME               1 (R)

  3           8 LOAD_CONST               2 ('\x1b[1;32m')
             10 STORE_NAME               2 (G)

  4          12 LOAD_CONST               3 ('\x1b[1;37m\x1b[34m')
             14 STORE_NAME               3 (B)

  5          16 LOAD_CONST               4 (0)
             18 LOAD_CONST               5 (None)
             20 IMPORT_NAME              4 (marshal)
             22 STORE_NAME               4 (marshal)

 15          24 LOAD_CONST               6 ("\n%s\n         _       _             \n   /\\  /(_) __ _| |__   /\\/\\   \n  / /_/ / |/ _` | '_ \\ /    \\  \n / __  /| | (_| | | | / /\\/\\ \\ \n \\/ /_/ |_|\\__, |_| |_\\/    \\/ \n           |___/               \n%s\n")
             26 LOAD_NAME                3 (B)
             28 LOAD_NAME                0 (N)
             30 BUILD_TUPLE              2
             32 BINARY_MODULO
             34 STORE_NAME               5 (banner)

 16          36 LOAD_NAME                6 (print)
             38 LOAD_NAME                5 (banner)
             40 CALL_FUNCTION            1
             42 POP_TOP

 17          44 LOAD_CONST               4 (0)
             46 STORE_NAME               7 (counter)

 18          48 LOAD_NAME                8 (input)
             50 LOAD_NAME                9 (str)
             52 LOAD_CONST               7 ('Path file » ')
             54 CALL_FUNCTION            1
             56 CALL_FUNCTION            1
             58 STORE_NAME              10 (file)

 19          60 LOAD_NAME                8 (input)
             62 LOAD_NAME                9 (str)
             64 LOAD_CONST               8 ('Any type » ')
             66 CALL_FUNCTION            1
             68 CALL_FUNCTION            1
             70 LOAD_METHOD             11 (encode)
             72 CALL_METHOD              0
             74 STORE_NAME              12 (any)

 20          76 LOAD_NAME               13 (int)
             78 LOAD_NAME                8 (input)
             80 LOAD_CONST               9 ('Count marshal » ')
             82 CALL_FUNCTION            1
             84 CALL_FUNCTION            1
             86 STORE_NAME              14 (count)

 21          88 LOAD_NAME               14 (count)
             90 LOAD_CONST              10 (400)
             92 COMPARE_OP               0 (<)
             94 POP_JUMP_IF_FALSE       98

 22          96 JUMP_FORWARD             6 (to 104)

 24     >>   98 LOAD_NAME               15 (exit)
            100 CALL_FUNCTION            0
            102 POP_TOP

 25     >>  104 LOAD_NAME                8 (input)
            106 LOAD_NAME                9 (str)
            108 LOAD_CONST              11 ('Output » ')
            110 CALL_FUNCTION            1
            112 CALL_FUNCTION            1
            114 STORE_NAME              16 (out)

 26         116 LOAD_NAME               17 (open)
            118 LOAD_NAME               10 (file)
            120 CALL_FUNCTION            1
            122 LOAD_METHOD             18 (read)
            124 CALL_METHOD              0
            126 STORE_NAME              19 (od)

 27         128 LOAD_NAME               20 (compile)
            130 LOAD_NAME               19 (od)
            132 LOAD_CONST              12 ('<%s>')
            134 LOAD_CONST              13 ('exec')
            136 LOAD_NAME               12 (any)
            138 BINARY_MODULO
            140 CALL_FUNCTION            3
            142 STORE_NAME              21 (cpanel)

 28         144 LOAD_NAME                4 (marshal)
            146 LOAD_METHOD             22 (dumps)
            148 LOAD_NAME               21 (cpanel)
            150 CALL_METHOD              1
            152 STORE_NAME              23 (dor)

 29         154 LOAD_NAME               24 (repr)
            156 LOAD_NAME               23 (dor)
            158 CALL_FUNCTION            1
            160 STORE_NAME              25 (results)

 30         162 LOAD_NAME               17 (open)
            164 LOAD_NAME               16 (out)
            166 LOAD_CONST              14 ('w')
            168 CALL_FUNCTION            2
            170 STORE_NAME              26 (s)

 31         172 LOAD_NAME               26 (s)
            174 LOAD_METHOD             27 (write)
            176 LOAD_CONST              15 ('import marshal\nexec(marshal.loads(')
            178 LOAD_NAME                9 (str)
            180 LOAD_NAME               25 (results)
            182 CALL_FUNCTION            1
            184 BINARY_ADD
            186 LOAD_CONST              16 ('))')
            188 BINARY_ADD
            190 CALL_METHOD              1
            192 POP_TOP

 32         194 LOAD_NAME               26 (s)
            196 LOAD_METHOD             28 (close)
            198 CALL_METHOD              0
            200 POP_TOP

 33         202 SETUP_LOOP             126 (to 330)
        >>  204 LOAD_NAME               14 (count)
            206 LOAD_NAME                7 (counter)
            208 COMPARE_OP               5 (>=)
            210 EXTENDED_ARG             1
            212 POP_JUMP_IF_FALSE      328

 34         214 LOAD_NAME               17 (open)
            216 LOAD_NAME               16 (out)
            218 CALL_FUNCTION            1
            220 LOAD_METHOD             18 (read)
            222 CALL_METHOD              0
            224 STORE_NAME              29 (ops)

 35         226 LOAD_NAME               20 (compile)
            228 LOAD_NAME               29 (ops)
            230 LOAD_CONST              12 ('<%s>')
            232 LOAD_CONST              13 ('exec')
            234 LOAD_NAME               12 (any)
            236 BINARY_MODULO
            238 CALL_FUNCTION            3
            240 STORE_NAME              30 (cc)

 36         242 LOAD_NAME                4 (marshal)
            244 LOAD_METHOD             22 (dumps)
            246 LOAD_NAME               30 (cc)
            248 CALL_METHOD              1
            250 STORE_NAME              31 (pp)

 37         252 LOAD_NAME               24 (repr)
            254 LOAD_NAME               31 (pp)
            256 CALL_FUNCTION            1
            258 STORE_NAME              32 (res)

 38         260 LOAD_NAME                6 (print)
            262 LOAD_CONST              17 ('%s%s%s')
            264 LOAD_NAME                1 (R)
            266 LOAD_NAME                7 (counter)
            268 LOAD_NAME                0 (N)
            270 BUILD_TUPLE              3
            272 BINARY_MODULO
            274 CALL_FUNCTION            1
            276 POP_TOP

 39         278 LOAD_NAME               17 (open)
            280 LOAD_NAME               16 (out)
            282 LOAD_CONST              14 ('w')
            284 CALL_FUNCTION            2
            286 STORE_NAME              33 (wrote)

 40         288 LOAD_NAME               33 (wrote)
            290 LOAD_METHOD             27 (write)
            292 LOAD_CONST              15 ('import marshal\nexec(marshal.loads(')
            294 LOAD_NAME                9 (str)
            296 LOAD_NAME               32 (res)
            298 CALL_FUNCTION            1
            300 BINARY_ADD
            302 LOAD_CONST              16 ('))')
            304 BINARY_ADD
            306 CALL_METHOD              1
            308 POP_TOP

 41         310 LOAD_NAME               33 (wrote)
            312 LOAD_METHOD             28 (close)
            314 CALL_METHOD              0
            316 POP_TOP

 42         318 LOAD_NAME                7 (counter)
            320 LOAD_CONST              18 (1)
            322 INPLACE_ADD
            324 STORE_NAME               7 (counter)
            326 JUMP_ABSOLUTE          204
        >>  328 POP_BLOCK

 43     >>  330 LOAD_NAME                6 (print)
            332 LOAD_CONST              19 ('%sSucces%s')
            334 LOAD_NAME                2 (G)
            336 LOAD_NAME                0 (N)
            338 BUILD_TUPLE              2
            340 BINARY_MODULO
            342 CALL_FUNCTION            1
            344 POP_TOP
            346 LOAD_CONST               5 (None)
            348 RETURN_VALUE
