def convert_string(s):
    if s == '':
        return ''
    else:
        string_list = list(s)
        start = 0
        end = 1
        word_list=[]
        while end < len(string_list):
            if string_list[end].isupper() or string_list[end] =='.':
                string_list[end] = string_list[end].lower()
                word_list.append(''.join(string_list[start:end]))
                start = end
            end += 1
        output = ' '.join(word_list)+'.'
        return output




