class VuWorker:
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path

    def process_audio(self, input_url, output_url):
        command = [self.ffmpeg_path, '-i', input_url, '-f', 'wav', output_url]
        subprocess.run(command)


class AudioManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AudioManager, cls).__new__(cls)
            cls._instance._is_playing = False
            cls._instance._current_audio = None
        return cls._instance

    def play(self, audio_file):
        if self._current_audio:
            self.stop()
        self._current_audio = audio_file
        self._is_playing = True
        # Implement audio playback logic here

    def stop(self):
        if self._is_playing:
            # Implement stop logic here
            self._is_playing = False


def format_url(base_url, endpoint):
    return f'{base_url}/{endpoint}'


def main():
    # Example usage of VuWorker and AudioManager
    worker = VuWorker('/usr/bin/ffmpeg')
    worker.process_audio('input.mp3', 'output.wav')
    audio_manager = AudioManager()
    audio_manager.play('output.wav')


if __name__ == '__main__':
    main()