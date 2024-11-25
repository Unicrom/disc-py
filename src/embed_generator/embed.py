import discord
import datetime

from src.embed_generator.embed_field import EmbedField
from src.embed_generator.embed_file import EmbedFile


class Embed:
    # TODO add method to generate discord Embed object

    def __init__(self, template: bool = False) -> None:
        """
        Creates an empty Embed object\n
        **template:** whether attributes should have placeholder values"""
        self.reset_type()
        if template:
            self.apply_template()

    # Name Methods
    def set_name(self, name: str) -> None:
        """
        Sets the Title of the Embed\n
        **name:** title of Embed"""
        self.name = name

    def clear_name(self) -> None:
        """
        Clears the title of the Embed"""
        self.name = None

    # Author Methods
    def set_author(
        self,
        author: str,
        url: str = None,
        icon_url: str = None,
        local_icon_url: bool = False,
    ) -> None:
        """
        Sets the Author of the Embed\n
        **author:** name of author *Max of 256 char*\n
        **url:** *optional* url for the author\n
        **icon_url:** *optional* URL of the author icon *Only Supports HTTP(s)*\n
        **local_icon_url** *optional* whether icon_url is a local path"""
        self.author = author
        self.author_url = url

        if icon_url:
            self.set_author_icon(icon_url, local_icon_url)
        else:
            self.author_icon_url = None

    def set_author_url(self, url: str) -> None:
        """
        Sets the URL of the author\n
        **url:** URL of author"""
        self.author_url = url

    def set_author_icon(self, url: str, local: bool = False) -> None:
        """
        Sets the icon for the author\n
        **url:** the URL for the img\n
        **local:** *optional* whether the URL is a local file path"""
        if not local:
            self.author_icon_url = url
            return

        local_path = self.add_local_file(url, return_new_path=True)
        self.author_icon_url = local_path

    def clear_author(self) -> None:
        """
        Clears the author of the Embed"""
        self.clear_author_name()
        self.clear_author_url()
        self.clear_author_icon()

    def clear_author_name(self) -> None:
        """
        Deletes the name of the Embed"""
        self.author = None

    def clear_author_url(self) -> None:
        """
        Deletes the Author URL"""
        self.author_url = None

    def clear_author_icon(self) -> None:
        """
        Deletes the Author icon"""
        if "attachment://" in self.author_icon_url:
            self.delete_file(self.author_icon_url)
        self.author_icon_url = None

    # Color Methods
    def set_color(self, value: str) -> None:
        """
        Sets the color of the Embed\n
        **value:** color code\n"""
        match "hex":  # Future plans to support different color formats
            case "hex":
                self.set_hex_color(value)
            case _:
                raise Exception("Color Format not Supported")

    def set_hex_color(self, value: str) -> None:
        """
        Sets the color of the Embed to a hex value\n
        **value:** hexadecimal code"""
        self.color = value

    def reset_color(self) -> None:
        """
        Sets the color to black"""
        self.color = self.set_color("000000")

    # Description Methods
    def set_desc(self, value: str, raise_error: bool = True) -> None:
        """
        Sets the description of the Embed\n
        **value:** description of embed *4096 char max*"""
        if 4096 < len(value) and raise_error:
            raise Exception("Description of Embed exceeds 4096 char limit")
        self.desc = value

    def clear_desc(self) -> None:
        """
        Clears the description of the Embed"""
        self.desc = None

    # Field Methods
    def create_field(
        self, label: str, content: str, index: int = -1, inline: bool = True
    ) -> None:
        """
        Adds a new Field to the embed\n
        **label:** name of field *256 char max*\n
        **content:** value of field *1024 char max*\n
        **index:** index of field
        > *default* -1 adds the field to the back\n
        **inline** *optional* whether the the field is displayed as inline"""
        new_field = EmbedField(label, content, inline)
        if index == -1:
            self.fields.append(new_field)
        else:
            self.fields.insert(index, new_field)

    def field_from_JSON(self, JSON: dict, index: int = -1) -> None:
        """
        Creates a field based on a JSON file\n
        **JSON:** the JSON code being used in generation\n
        **index:** *optional* index of the Field *default -1 = add to end of fields*"""
        self.create_field(JSON["label"], JSON["content"], index, JSON["inline"])

    def clear_fields(self) -> None:
        """
        Clears the Fields of the Embed"""
        self.fields = []

    def delete_field(self, field_label: str, delete_all: bool = True) -> None:
        """
        Deletes a fields under a specified label\n
        **field_label:** label of field being deleted\n
        **delete_all:** *optional* whether all fields of said label are deleted"""
        for field in self.fields:
            if not field.label == field_label:
                continue

            self.fields.remove(field)
            if not delete_all:
                return

    # Footer Methods
    def set_footer(
        self, content: str, icon_url: bool = None, local_icon_url: bool = False
    ) -> None:
        """
        Sets the Footer of the Embed\n
        **content:** text of the footer *Max of 0248 char*\n
        **icon_url:** *optional* URL of the footer icon *Only Supports HTTP(s)*\n
        **local_icon_url** *optional* whether icon_url is a local path"""
        self.footer_content = content
        if icon_url:
            self.set_footer_icon(icon_url, local_icon_url)
        else:
            self.footer_icon_url = None

    def set_footer_icon(self, url: str, local: bool = False) -> None:
        """
        Sets the icon for the footer\n
        **url:** the URL for the img\n
        **local:** *optional* whether the URL is a local file path"""
        if not local:
            self.footer_icon_url = url
            return

        local_path = self.add_local_file(url, return_new_path=True)
        self.footer_icon_url = local_path

    def clear_footer(self) -> None:
        """
        Clears the Footer of the Embed"""
        self.clear_footer_content()
        self.clear_footer_icon()

    def clear_footer_content(self) -> None:
        """
        Clears the content of the Footer"""
        self.footer_content = None

    def clear_footer_icon(self) -> None:
        """
        Deletes the Footer icon"""
        if "attachment://" in self.footer_icon_url:
            self.delete_file(self.footer_icon_url)
        self.footer_icon_url = None

    # Type Methods
    def set_type(self, type: str) -> None:
        """
        Sets the type of the Embed\n
        **type:** type being set to"""
        self.type = type

    def reset_type(self) -> None:
        """
        Sets the type of the Embed to Rich"""
        self.set_type("Rich")

    # File Methods
    def add_local_file(self, file_path: str, return_new_path: bool = True):
        """
        Adds a local file that can be used for media assets within the embed\n
        **file_path:** path to the file\n
        **return_new_path:** whether the new \'attachment://\' should be returned"""
        new_file = EmbedFile(file_path)
        self.files.append(new_file)

        if return_new_path:
            return new_file.get_attachment_url()

    def clear_files(self) -> None:
        """
        Clears the content of files"""
        self.files = []

    def delete_file(self, file_path: str) -> None:
        """
        Removes a file based on a target file_path\n
        **file_path:** the \'attachment//:\' path of the file being removed"""
        for file in self.files:
            if file.get_attachment_url() == file_path:
                self.files.remove(file)

    # Image Methods
    def set_image(self, url: str, local: bool = False) -> None:
        """
        Sets the image for the embed content\n
        **url:** URL of the img\n
        **local:** *optional* whether the URl is a local path"""
        if not local:
            self.image_url = url
        else:
            local_image_url = self.add_local_file(url)
            self.image_url = local_image_url

    def clear_image(self) -> None:
        """
        Clears the Image of the Embed"""
        if "attachment://" in self.image_url:
            self.delete_file(self.image_url)
        self.image_url = None

    # Thumbnail Method
    def set_thumbnail(self, url: str, local: bool = False) -> None:
        """
        Sets the thumbnail for the embed content\n
        **url:** URL of the thumbnail\n
        **local:** *optional* whether the URl is a local path"""
        if not local:
            self.thumbnail_url = url
        else:
            local_thumbnail_url = self.add_local_file(url)
            self.thumbnail_url = local_thumbnail_url

    def clear_thumbnail(self) -> None:
        """
        Clears the thumbnail of the Embed"""
        if "attachment://" in self.thumbnail_url:
            self.delete_file(self.thumbnail_url)
        self.thumbnail_url = None

    # URL Methods
    def set_url(self, url: str) -> None:
        """
        Sets the url of the embed\n
        **url:** url of embed"""
        self.url = url

    def clear_url(self) -> None:
        """
        Clears the url of the Embed"""
        self.url = None

    # Timestamp Methods
    def set_timestamp(self, datetime: datetime.datetime) -> None:
        """
        Sets the timestamp for the embed to an aware datetime\n
        **datetime:** the datetime.datetime object timestamp is being set to"""
        self.timestamp = datetime

    def clear_timestamp(self) -> None:
        """
        Clears the timestamp of the Embed"""
        self.timestamp = None

    # Misc Methods
    def clear_content(self, clear_name: bool = True) -> None:
        """
        Clears the values of the embed\n
        **clear_name:** whether the name is cleared"""
        if clear_name:
            self.clear_name()  # Clear Title

        self.clear_author()
        self.reset_color()
        self.clear_desc()
        self.clear_fields()
        self.clear_footer()
        self.clear_image()
        self.clear_thumbnail()
        self.clear_timestamp()
        self.reset_type()
        self.clear_url()

        self.clear_files()

    def apply_template(self) -> None:
        """
        Filles the Embed with placeholder values\n
        **WARNING** *completely clears embed attributes*"""
        self.clear_content(True)  # Clears Embed Content

        self.set_name("Embed Title")
        self.set_author("User123")
        self.set_color("ff0000")
        self.set_desc("Description of Embed")
        self.set_footer("Footer of Embed")
        self.reset_type()

    # JSON Methods
    def to_JSON(self) -> dict:
        """
        Generates a JSON code with embed attributes"""
        fields_JSON = [field.to_JSON() for field in self.fields]
        files_JSON = [file.to_JSON() for file in self.files]

        embed_JSON = {
            "author": {
                "name": self.author,
                "url": self.author_url,
                "icon": self.author_icon_url,
            },
            "color": self.color,
            "desc": self.desc,
            "fields": fields_JSON,
            "footer": {"content": self.footer_content, "icon": self.footer_icon_url},
            "image": self.image_url,
            "thumbnail": self.thumbnail_url,
            "timestamp": self.timestamp,
            "name": self.name,
            "type": self.type,
            "url": self.url,
            "files": files_JSON,
        }

        return embed_JSON

    def from_JSON(self, embed_JSON: dict) -> None:
        """
        Sets the embeds properties based on JSON code\n
        **embed_JSON:** JSON for the embed"""
        self.set_author(
            embed_JSON["author"]["name"],
            embed_JSON["author"]["url"],
            embed_JSON["author"]["icon"],
        )
        self.set_color(embed_JSON["color"])
        self.set_desc(embed_JSON["desc"])
        self.set_image(embed_JSON["image"])
        self.set_thumbnail(embed_JSON["thumbnail"])
        self.set_name(embed_JSON["name"])
        self.set_type(embed_JSON["type"])
        self.set_url(embed_JSON["url"])
        self.set_timestamp(embed_JSON["timestamp"])

        self.clear_fields()
        self.clear_files()
        for field_JSON in embed_JSON["fields"]:
            self.field_from_JSON(field_JSON)
        for file_JSON in embed_JSON["files"]:
            self.add_local_file(file_JSON["path"], return_new_path=False)

    # Embed Generation Methods
    def create_embed_object(self) -> None:
        '''
        Creates an discord.Embed object and sets the different properties'''
        discord_embed = discord.Embed(
            color=self.color,
            title=self.name,
            type=self.type,
            url=self.url,
            description=self.desc,
            timestamp=self.timestamp,
        )

        for field in self.fields:
            discord_embed.add_field(field.label, field.content, field.inline)
        discord_embed.set_author(self.author, url=self.author_url, icon_url=self.author_icon_url)
        discord_embed.set_footer(text=self.footer_content, icon_url=self.footer_icon_url)
        discord_embed.set_image(self.image_url)
        discord_embed.set_thumbnail(self.thumbnail_url)

        self.discord_embed = discord_embed
    
    def create_file_objects(self) -> None:
        '''
        Creates a list of discord.File objects'''
        self.discord_files = [
            file.generate_discord_object for file in self.files
        ]

    def generate(self) -> list:
        '''
        Returns a list in the format of [discord.Embed, [...discord.File]]'''
        self.create_embed_object()
        self.create_file_objects()

        return [self.discord_embed, self.discord_files]
