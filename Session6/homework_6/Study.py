from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

# option = {
#     'format':'bestaudio/audio'
# }
# dl = YoutubeDL(option)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

# option = {
#     'default_search':'ytsearch',
#     'max_download':1
# }
# dl = YoutubeDL(option)
# dl.download(['con điên TAMKA PKL'])

option = {
    'default_search':'ytsearch',
    'max_download':1,
    'format':'bestaudio/audio'
}
dl = YoutubeDL(option)
dl.download(['Nhớ mưa sài gòn lam trường'])
