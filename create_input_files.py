from utils_local import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
                       karpathy_json_path='caption_datasets/dataset_coco.json',
                       image_folder='2014/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='output/',
                       max_len=50)
