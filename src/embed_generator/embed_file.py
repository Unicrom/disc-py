import discord

class EmbedFile:
    def __init__(self, path: str) -> None:
        """
        Creates a special file object easily accessed by Embeds object\n
        **path:** path to file *must contain file name*"""
        self.change_file_path(path)

    def get_file_name(self) -> None:
        """
        Extracts file name from the path"""
        path = self.path
        if "/" in path:  # Path uses / as a separator
            separated_path = path.split("/")
            self.file_name = separated_path[-1]
        elif "\\" in path:  # Path uses \ as a separator
            separated_path = path.split("/")
            self.file_name = separated_path[-1]
        else:  # If the path is also the file name
            self.file_name = path

    def get_attachment_url(self) -> str:
        """
        Returns a str to be used in specifying the use of a local image"""
        attachment_path = "attachment://" + self.file_name
        return attachment_path

    def change_file_path(self, path: str) -> None:
        """
        Changes the path of the file\n
        **path:** new file path"""
        self.path = path
        self.get_file_name()

    def generate_discord_object(self) -> discord.File:
        """
        Creates a discord.File object"""
        file = discord.File(self.path, self.file_name)
        return file
