# # def inputs(video_file,vocal_file,quality,output_height,use_previous_tracking_data,wav2lip_version,nosmooth,U,D,L,R,)
import configparser

def save_easy_wav2lip_config(
    video_file,
    vocal_file,  # Optional
    quality,
    output_height="full resolution",
    use_previous_tracking_data=True,
    wav2lip_version="Wav2Lip_GAN",
    nosmooth=True,
):
    """
    Saves Easy-Wav2Lip configuration options to a specified INI file.

    Args:
        video_file (str): Path to the video file.
        vocal_file (str, optional): Path to the audio file (defaults to "").
        quality (str, optional): Wav2Lip quality setting (defaults to "Enhanced").
        output_height (str, optional): Output video height (defaults to "full resolution").
        use_previous_tracking_data (bool, optional): Reuse previous tracking data (defaults to True).
        wav2lip_version (str, optional): Wav2Lip version to use (defaults to "Wav2Lip_GAN").
        nosmooth (bool, optional): Disable smoothing (defaults to True).
        padding_up (int, optional): Padding around the top of the face (defaults to 0).
        padding_down (int, optional): Padding around the bottom of the face (defaults to 0).
        padding_left (int, optional): Padding around the left side of the face (defaults to 0).
        padding_right (int, optional): Padding around the right side of the face (defaults to 0).
        mask_size (float, optional): Size of the mouth mask (defaults to 2.5).
        mask_feathering (int, optional): Feathering amount for the mask (defaults to 2).
        mouth_tracking (bool, optional): Enable mouth tracking (defaults to False).
        debug_mask (bool, optional): Show debugging information about the mask (defaults to False).
        batch_process (bool, optional): Enable batch processing (defaults to False).
        output_suffix (str, optional): Suffix for output video filename (defaults to "_Easy-Wav2Lip").
        include_settings_in_suffix (bool, optional): Include settings in output filename suffix (defaults to False).
        preview_input (bool, optional): Preview only the input video (defaults to False).
        preview_settings (bool, optional): Preview only the processed first frame (defaults to False).
        frame_to_preview (int, optional): Frame number for preview if `preview_settings` is True (defaults to 100).
        config_file (str, optional): Path to the INI configuration file to write to (defaults to "config.ini").
    """

    config = configparser.ConfigParser()

    # Create sections with clear names
    config['OPTIONS'] = {}
    config['PADDING'] = {}
    config['MASK'] = {}
    config['OTHER'] = {}

    # Add configuration options to appropriate sections
    config['OPTIONS']['video_file'] = video_file
    config['OPTIONS']['vocal_file'] = vocal_file
    config['OPTIONS']['quality'] = quality
    config['OPTIONS']['output_height'] = output_height
    config['OPTIONS']['use_previous_tracking_data'] = str(use_previous_tracking_data)  # Convert bool to string
    config['OPTIONS']['wav2lip_version'] = wav2lip_version
    config['OPTIONS']['nosmooth'] = str(nosmooth)  # Convert bool to string

    config['PADDING']['U'] = str(0)
    config['PADDING']['D'] =str(0)
    config['PADDING']['L'] = str(0)
    config['PADDING']['R'] = str(0)

    config['MASK']['size']=str(2.5)
    config['MASK']['feathering']=str(2)
    config['MASK']['mouth_tracking']=str(True)
    config['MASK']['debug_mask']=str(False)

    config['OTHER']['batch_process']= str(False)
    config['OTHER']['output_suffix']= "_Easy-Wav2Lip"
    config['OTHER']['include_settings_in_suffix ']= str(False)
    config['OTHER']['preview_input']= str(False)
    config['OTHER']['preview_settings']= str(False)
    config['OTHER']['frame_to_preview']= str(1000)

    with open('config.ini', 'w') as f:
      config.write(f)

    return True

# # @markdown On destktop: <h1></h1>Click the folder icon ( 📁 ) at the left edge of colab, find your file, right click, copy path, paste it below:
# #@markdown<br></br>
# # @markdown On mobile: <h1></h1>Tap the hamburger button ( ☰ ) at the top left, click show file browser, find your file, long press on it, copy path, paste below:
# video_file = "/content/drive/MyDrive/imaginary_conversation.mp4" #@param {type:"string"}
# vocal_file = "/content/translated.wav" #@param {type:"string"}

# #@markdown > Keep vocal_file blank if your video already has the desired speech audio encoded into it.
# #@markdown # Quality
# quality = "Enhanced" # @param ["Fast", "Improved", "Enhanced", "Experimental"]
# #@markdown * <b><u>Fast</u></b>: Wav2Lip <br>
# #@markdown * <b><u>Improved</u></b>: Wav2Lip with a feathered mask around the mouth to remove the square around the face <br>
# #@markdown * <b><u>Enhanced</u></b>: Wav2Lip + mask + GFPGAN upscaling done on the face
# #@markdown * <b><u>Experimental</u></b>: Test version of applying gfpgan - see [release notes](https://github.com/anothermartz/Easy-Wav2Lip/releases/tag/v7_release)
# #preview_quality = False #@param {type:"boolean"} - coming soon!
# output_height = "full resolution" #@param ["half resolution", "full resolution", "480"] {allow-input: true}
# use_previous_tracking_data = True #@param {type:"boolean"}
# #@markdown Speeds up processing of the same video used multiple times - it should delete the last tracking file automatically when the video is changed but if it's failing after the first video, untick this box.

# #@markdown
# #------------------------------*Step 3*----------------------------------------!
# #@markdown <h1>👈 Step 3:  Click the little circle play button on this cell! </h1> (Or press ctrl + F10) - Then wait for processing to complete.
# # scale padding with resolution
# #@markdown <br>

# #@markdown ---
# #@markdown <br>

# #@markdown # [Advanced tweaking](https://github.com/anothermartz/Easy-Wav2Lip/tree/v7#advanced-tweaking) (optional) </h1>Just ignore all of this if you are new, or click the blue titles for instructions.
# wav2lip_version = "Wav2Lip_GAN" # @param ["Wav2Lip", "Wav2Lip_GAN"]
# nosmooth = True #@param {type:"boolean"}
# #@markdown ### [Padding:](https://github.com/anothermartz/Easy-Wav2Lip/tree/v7#padding)</h1> (Up, Down, Left, Right) <br>
# U = 0 #@param {type:"slider", min:-100, max:100, step:1}
# D = 0 #@param {type:"slider", min:-100, max:100, step:1}
# L = 0 #@param {type:"slider", min:-100, max:100, step:1}
# R = 0 #@param {type:"slider", min:-100, max:100, step:1}
# #@markdown <br>

# #@markdown ### [Mask:](https://github.com/anothermartz/Easy-Wav2Lip/tree/v7#other-options)
# size = 2.5 #@param {type:"slider", min:1, max:6, step:0.1}
# feathering = 2 #@param {type:"slider", min:0, max:3, step:1}
# mouth_tracking = False #@param {type:"boolean"}
# debug_mask = False #@param {type:"boolean"}


# #@markdown # [Other options:](https://github.com/anothermartz/Easy-Wav2Lip/tree/v7#other-options)

# batch_process = False #@param {type:"boolean"}
# output_suffix = "_Easy-Wav2Lip" #@param {type:"string"}
# include_settings_in_suffix = False #@param {type:"boolean"}
# preview_input = False #@param {type:"boolean"}
# preview_settings = False #@param {type:"boolean"}
# #@markdown preview_settings processes only one frame so you can see how it looks without doing the whole video
# frame_to_preview = 100 # @param {type:"integer"}


# import configparser

# # Create a ConfigParser object
# config = configparser.ConfigParser()

# # Put all your variables in a dictionary
# options = {
#     'video_file': video_file,
#     'vocal_file': vocal_file,
#     'quality': quality,
#     'output_height': output_height,
#     'wav2lip_version': wav2lip_version,
#     'use_previous_tracking_data': use_previous_tracking_data,
#     'nosmooth': nosmooth
# }
# padding = {
#     'U': U,
#     'D': D,
#     'L': L,
#     'R': R
# }
# mask = {
#     'size': size,
#     'feathering': feathering,
#     'mouth_tracking': mouth_tracking,
#     'debug_mask': debug_mask
# }
# other = {
#     'batch_process': batch_process,
#     'output_suffix': output_suffix,
#     'include_settings_in_suffix': include_settings_in_suffix,
#     'preview_input': preview_input,
#     'preview_settings': preview_settings,
#     'frame_to_preview': frame_to_preview
# }


# # Add the dictionary to the ConfigParser object
# config['OPTIONS'] = options
# config['PADDING'] = padding
# config['MASK'] = mask
# config['OTHER'] = other

# # Write the data to an INI file
# with open('config.ini', 'w') as f:
#     config.write(f)
