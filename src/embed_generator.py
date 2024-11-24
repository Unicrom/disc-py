import discord


class Embed:
    # TODO add method to set Embed image
    # TODO add method to set Embed Provider
    # TODO add rgb and hsl support to set_color method
    # TODO add add_local_file' method to generate local file paths '
    # TODO add method to set Embed thumbnail
    # TODO add method to set Embed timestamp
    # TODO add method to set Embed url
    # TODO add method to set Embed video
    # TODO add method to set Author Icon
    # TODO add method to set Footer Icon
    # TODO add method to create field from JSON
    # TODO add method to create JSON from field
    # TODO add method to generate Embed object from JSON
    # TODO add method to generate JSON from Embed object
    # TODO add method to create discord File object from local files
    # TODO add method to generate discord Embed object 

    def __init__(self, name: str, template: bool = False) -> None:
        """
        #### Creates an empty Embed object
        **name:** title of Discord Embed\n
        **template:** whether attributes should have placeholder values"""
        self.set_name(name)
        self.reset_type()

        if template: self.apply_template()

    def clear_content(self, clear_name: bool = True) -> None:
        """
        #### Clears the values of the embed
        **clear_name:** whether the name is cleared"""
        if clear_name:
            self.clear_name()  # Clear Title

        self.clear_author()
        self.reset_color()
        self.clear_desc()
        self.clear_fields()
        self.clear_footer()
        self.clear_img()
        self.clear_provider()
        self.clear_thumbnail()
        self.clear_timestamp()
        self.reset_type()
        self.clear_url()
        self.clear_video()

    def apply_template(self) -> None:
        """
        #### Filles the Embed with placeholder values
        **WARNING** *completely clears embed attributes*"""
        self.clear_content(True)  # Clears Embed Content

        self.set_name("Embed Title")
        self.set_author("User123")
        self.set_color("ff0000")
        self.set_desc("Description of Embed")
        self.set_footer("Footer of Embed")
        self.reset_type()

    # Set Fields
    def set_name(self, name: str) -> None:
        """
        #### Sets the Title of the Embed
        **name:** title of Embed"""
        self.name = name

    def set_author(self, author: str, url: str = None, icon_url: str = None) -> None:
        """
        #### Sets the Author of the Embed
        **author:** name of author *Max of 256 char*\n
        **url:** *optional* url for the author\n
        **icon_url:** *optional* URL of the author icon *Only Supports HTTP(s)*\n
        ##### Set icon to a local file:
        > use **add_local_img** method with **target=\'author\'** *requires img path*"""
        self.author = author
        self.author_url = url
        self.author_icon_url = icon_url

    def set_color(self, value: str, format: str = "hex") -> None:
        """
        #### Sets the color of the Embed
        **value:** color code\n
        **format:** *optional* format of color code\n
        *possible values:* `default` \'hex\'"""
        match format:
            case "hex":
                self.set_hex_color(value)
            case _:
                raise Exception("Color Format not Supported")

    def set_hex_color(self, value: str) -> None:
        """
        #### Sets the color of the Embed to a hex value
        **value:** hexadecimal code"""
        self.color = value

    def set_desc(self, value: str, raise_error: bool = True) -> None:
        """
        #### Sets the description of the Embed
        **value:** description of embed *4096 char max*"""
        if 4096 < len(value) and raise_error:
            raise Exception("Description of Field exceeds 4096 char limit")
        self.desc = value

    def create_field(
        self, label: str, content: str, index: int = -1, inline: bool = True
    ) -> None:
        """
        #### Adds a new Field to the embed
        **label:** name of field *256 char max*\n
        **content:** value of field *1024 char max*\n
        **index:** index of field
        > *default* -1 adds the field to the back\n
        **inline** *optional* whether the the field is displayed as inline"""
        new_field = Field(label, content, inline)
        if index == -1:
            self.fields.append(new_field)
        else:
            self.fields.insert(index, new_field)

    def set_footer(self, content: str, icon_url: bool = None) -> None:
        """
        #### Sets the Footer of the Embed
        **content:** text of the footer *Max of 0248 char*\n
        **icon_url:** *optional* URL of the footer icon *Only Supports HTTP(s)*\n
        ##### Set icon to a local file:
        > use **add_local_img** method with **target=\'footer\'** *requires img path*"""
        self.footer_content = content
        self.footer_icon_url = icon_url

    def set_type(self, type: str) -> None:
        """
        #### Sets the type of the Embed
        **type:** type being set to"""
        self.type = type

    # Clear Fields
    def clear_name(self) -> None:
        """
        #### Clears the title of the Embed"""
        self.name = None

    def clear_author(self) -> None:
        """
        #### Clears the author of the Embed"""
        self.author = None
        self.author_url = None
        self.author_icon_url = None

    def reset_color(self) -> None:
        """
        #### Sets the color to black"""
        self.color = self.set_color("000000")

    def clear_desc(self) -> None:
        """
        #### Clears the description of the Embed"""
        self.desc = None

    def clear_fields(self) -> None:
        """
        #### Clears the Fields of the Embed"""
        self.fields = []

    def clear_footer(self) -> None:
        """
        #### Clears the Footer of the Embed"""
        self.footer_content = None
        self.footer_icon_url = None

    def clear_img(self) -> None:
        """
        #### Clears the Image of the Embed"""
        self.img = None

    def clear_provider(self) -> None:
        """
        #### Clears the Provider of the Embed"""
        self.provider = None

    def clear_thumbnail(self) -> None:
        """
        #### Clears the thumbnail of the Embed"""
        self.thumbnail = None

    def clear_timestamp(self) -> None:
        """
        #### Clears the timestamp of the Embed"""
        self.timestamp = None

    def reset_type(self) -> None:
        """
        #### Sets the type of the Embed to Rich"""
        self.set_type("Rich")

    def clear_url(self) -> None:
        """
        #### Clears the url of the Embed"""
        self.url = None

    def clear_video(self) -> None:
        """
        #### Clears the video of the Embed"""
        self.video = None

    # Create Discord Objects
    def create_embed_object(self):
        discord_embed = discord.Embed()

    def generate(self) -> discord.Embed:
        discord_embed = discord.Embed()


class Field:
    def __init__(self, label: str, content: str, inline: bool = True) -> None:
        """
        #### Creates an embed Field Object
        **label:** name of field\n
        **content:** content of field\n
        **inline:** *optional* whether the field is displayed as inline"""
        self.label = self.set_label(label)
        self.content = self.set_content(content)
        self.inline = inline

    def set_label(self, label: str, raise_error: bool = True) -> None:
        """
        #### Sets the name of the field
        **label:** what the name of the field is set to *256 char max*\n
        **raise_error:** *optional* whether an Error is raised if label exceeds 256 char
        """
        if 256 < len(label) and raise_error:
            raise Exception("Label of Field exceeds 256 char limit")
        self.label = label

    def set_content(self, content: str, raise_error: bool = True) -> None:
        """
        #### Sets the value of the field
        **content:** what the value of the field is set to *1024 char max*\n
        **raise_error:** *optional* whether an Error is raised if content exceeds 1024 char
        """
        if 1024 < len(content) and raise_error:
            raise Exception("content of Field exceeds 1024 char limit")
        self.content = content

    def set_inline(self) -> None:
        """
        #### Sets the Field to be displayed as inline"""
        self.inline = True

    def set_block(self) -> None:
        """
        #### Sets the Field to be displayed as block"""
        self.inline = False
