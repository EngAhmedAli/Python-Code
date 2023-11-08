import json
def data_from_json(file_url):
    with open(file_url, 'r') as file:
        result = [json.loads(x) for x in file.readlines()]
    out_file = open('D:\\lab7_files\\Output_File.txt', 'a')
    for i in range(len(result)):
            if 'created_at' in result[i]:
                out_file.write('created_at : ' + str(result[i]['created_at']))
                out_file.write(',')
                out_file.write('Text : ' + str(result[i]['text'].encode('ascii', 'ignore')))
                out_file.write(',')
                out_file.write('User Name : ' + str(result[i]['user']['screen_name']))
                out_file.write('\n')

    out_file.close()
data_from_json('D:\\lab7_files\\TweetsPart1.txt')
data_from_json('D:\\lab7_files\\TweetsPart2.txt')
data_from_json('D:\\lab7_files\\TweetsPart3.txt')