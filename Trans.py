
#from google.cloud import translate


def translate():
    filename='E:\\Joscar\'s-Repo\\TransUsingGoogleAPI\\test.full.tsv'
    F = open(filename, 'r')
    output = open('data.txt', 'w')

    lines = F.readlines()
    for line in lines:
        l = line.split('\t')
        sen = l[1]
        result = Google_T(sen)
        output.write(result+' \t')
        sen = l[2]
        sen.replace("\n", "")
        result = Google_T(sen)
        output.write(result + ' \t')
        result = l[0]
        output.write(result + ' \n')

    output.close()
    F.close()


def Google_T(sen):
    translate_client = translate.Client()
    target = 'zh-CN'
    translation = translate_client.translate(
        sen,
        target_language=target)

    return translation['translatedText']



if __name__ == '__main__':
    translate()