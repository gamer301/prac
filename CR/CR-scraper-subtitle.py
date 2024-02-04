from youtube_transcript_api import YouTubeTranscriptApi


video_id1='OKLVLVlGqM0'
video_id2='GMcSxTyIzV4'

transcript1 = YouTubeTranscriptApi.get_transcript(video_id1)
transcript2 = YouTubeTranscriptApi.get_transcript(video_id2)



t1,t2=''

for x in transcript:
  sentence = x['text']
  output += f' {sentence}'

output.lower()
print(output)


with open('test0.txt','a+') as file:
  file.write(output)
