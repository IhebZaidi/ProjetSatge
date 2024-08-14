from pathlib import Path

class FileManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.plot_dir = Path("plots")
            cls._instance.plot_dir.mkdir(exist_ok=True)
        return cls._instance

    def get_file_path(self, file_name: str) -> Path:
        return self.plot_dir / file_name
