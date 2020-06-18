from manimlib.scene.scene import Scene
import threading
import time


class RawFrameScene(Scene):
    CONFIG = {
        "num_frames": 0,
        "msg_flag": True
    }

    def write_frame(self, frame):
        self.file_writer.write_frame(frame)

    def capture(self, mobjects, write_current_frame=True):
        self.update_frame(mobjects, self.get_frame())
        if write_current_frame:
            self.write_frame(self.get_frame())
            self.num_frames += 1
        return self

    def print_frame_message(self, msg_end="\r"):
        print("Capturing raw frame: {}".format(self.num_frames), end=msg_end)

    def setup_thread(self):
        def thread_func():
            while self.msg_flag:
                self.print_frame_message()
                time.sleep(1)

        thread = threading.Thread(target=thread_func, daemon=True)
        setattr(self, "msg_thread", thread)

    def __setup(self):
        self.file_writer.open_movie_pipe()
        self.setup_thread()
        self.msg_thread.start()

    # If this method is override, call __setup() manually
    def setup(self):
        self.__setup()

    def __end(self):
        self.file_writer.close_movie_pipe()
        setattr(self, "msg_flag", False)
        self.msg_thread.join()
        self.print_frame_message(msg_end="\n")
        self.num_plays += 1

    # If this method is override, call __end() manually
    def tear_down(self):
        self.__end()

    def play(self, *args, **kwargs):
        raise Exception("""
            'play' method is not allowed to use in this scene
        """)

    def wait(self, *args, **kwargs):
        raise Exception("""
            'wait' method is not allowed to use in this scene
        """)
