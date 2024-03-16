from moviepy.editor import VideoFileClip

def remove_audio(video_path, output_path):
    # Cargamos el video
    video_clip = VideoFileClip(video_path)
    
    # Eliminamos el audio
    video_clip_without_audio = video_clip.set_audio(None)
    
    # Guardamos el nuevo video sin audio
    video_clip_without_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Liberamos los recursos
    video_clip.close()
    video_clip_without_audio.close()

# Ruta al archivo de video de entrada
video_input_path = "C:/Users/Administrador/Downloads/Integraciones/ArchivosHarCX/HAR - Requerimiento ORACLE-20240315_093726-Meeting Recording.mp4"

# Ruta al archivo de video de salida (sin audio)
video_output_path = "C:/Users/Administrador/Downloads/Integraciones/ArchivosHarCX/HAR2.mp4"

# Llamamos a la función para eliminar el audio
remove_audio(video_input_path, video_output_path)

print("Proceso completado. Se ha eliminado el audio del video.")
