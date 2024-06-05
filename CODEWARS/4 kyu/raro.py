def path_finder(inputs):
    results = [0, 0]
    
    for input_str in inputs:
        for i in range(len(input_str)):
            if input_str[i].isdigit():
                num = int(input_str[i])
                if i > 0:
                    prev_char = input_str[i - 1]
                    if prev_char == 'r':
                        results[0] -= num
                    elif prev_char == 'R':
                        results[0] += num
                    elif prev_char == 'l':
                        results[1] += num
                    elif prev_char == 'L':
                        results[1] -= num
                        
        #print(f"Input: {input_str}, Result: {results}")
    
    return results

# Example strings
inputs = [
    '',
    'RLrl',
    'r5L2l4',
    'r5L2l4',
    '10r5r0',
    '10r5r0',
    'll60',
    'llll46lr',
    'l35lRRrl41r80r96r57l40r5l',
    'R71l32R66RR93lRRl74r99',
    'Rr95rR33lRr98R',
    'R60lll33',
    'r77lll33llr39',
    'll30r',
    'r41lR95r4R39l',
    'rrR54l74l8R',
    'lR44',
    'lr14l21l62lRll',
    'lRlR21lRlRl91l47r',
    'l0rlll29',
    'R11l60',
    'R0RR97',
    'r77lll12l3l85',
    'lR51l11R29r',
    'l34R71ll86r91',
    'rll100l24l92Rrl14',
    'l35Rl72RR',
    'lRll22l65lr',
    'R58RR74r28',
    'Rlll12r58RRRR3rR69',
    'lr30R15l84l87R',
    'lR',
    'l75l50lrlllrl0l14l',
    'l92lr91llll53l77R69lr44',
    'r44rrllR20R62l85l30',
    'r75RRl68R80rRr40rR16RR',
    'lrrl66R60rll68Rr94lr',
    'l76l86l87rll12r13l64lR2R54r',
    'Rl24r31llr37l87R85ll29l95l51',
    'r33l',
    'll',
    'Rl61llr99rl',
    'R99rRl60RRR38r17l',
    'lR18lRl22R24rl48',
    'l97rr53l26ll96RR97rR',
    'R16l',
    'lR9R82',
    'lR22',
    'lRl81ll13r90RR83',
    'll40ll69ll2'
]

# Processing inputs
for input_str in inputs:
    results = path_finder([input_str])
    print(f"Input: {input_str}, Result: {results}")
