
class instagramV1:
    def reels(self):
        print("you can post the reel")

class instagramV2(instagramV1):
    def story(self):
        print("you can upload a story")

print('raj - instagramV1')
raj = instagramV1()
raj.reels()


print('govind - instagramV2')
govind = instagramV2()
govind.reels()
govind.story()
