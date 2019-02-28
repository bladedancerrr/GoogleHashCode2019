from init import getPhotoList
from createSlideshow import createSlideshow
from createOutput import createOutput

def main():
	photoList = getPhotoList('c')
	slideshow = createSlideshow(photoList)
	createOutput(slideshow)

if __name__ == '__main__':
	main()