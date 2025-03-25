import util
import os
import moviepy as mp


def unisciVoceMusica(vocePath: str, musicaPath: str):

    outputFilePath = util.getAudioOutputFilePath()

    if not os.path.exists(vocePath):
        raise Exception("Il file con la voce non esiste")
    if not os.path.exists(musicaPath):
        raise Exception("Il file con la musica non esiste")

    voce = mp.AudioFileClip(vocePath)
    musica = mp.AudioFileClip(musicaPath).subclipped(0, voce.duration)

    audio = mp.CompositeAudioClip([musica, voce])

    audio.write_audiofile(outputFilePath)

    return outputFilePath


def unisciAudioVideo(audioPath: str, videoPath: str):

    outputFilePath = util.getVideoOutputFilePath()

    if not os.path.exists(audioPath):
        raise Exception("Il file con l'audio non esiste")
    if not os.path.exists(videoPath):
        raise Exception("Il file con il video non esiste")

    audio = mp.AudioFileClip(audioPath)
    video = mp.VideoFileClip(videoPath)

    if audio.duration > video.duration:
        audio = audio.subclipped(0, video.duration)
        
    if video.duration > audio.duration:
        video = video.subclipped(0, audio.duration)

    video.audio = audio

    video.write_videofile(outputFilePath)

    return outputFilePath
