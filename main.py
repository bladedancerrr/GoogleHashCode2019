from init import getPhotoList
from createSlideshow import createSlideshow
from createOutput import createOutput


def main():
	photoList = getPhotoList('c')
	slideshow = createSlideshow(photoList)
	slideshow.sort(key=lambda x: x.tagNumber, reverse=True)
	createOutput(slideshow)

if __name__ == '__main__':
	main()