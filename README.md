<div align="center">

   [![Python](https://img.shields.io/badge/Language-Python-blue?style=plastic)](https://en.wikipedia.org/wiki/Python_(programming_language))
   [![LOL](https://img.shields.io/badge/Game-League%20of%20Legends-445fa5.svg?style=plastic)](https://www.leagueoflegends.com/vi-vn/)
   [![Windows](https://img.shields.io/badge/Platform-Windows-0078d7.svg?style=plastic)](https://en.wikipedia.org/wiki/Microsoft_Windows)
   [![x64](https://img.shields.io/badge/Arch-x64-red.svg?style=plastic)](https://en.wikipedia.org/wiki/X86-64)
  
   # **[![Typing SVG](https://readme-typing-svg.demolab.com/?lines=+++++++++Ultilities+LOL+-+Thanks+for+using)](https://git.io/typing-svg)**

   <img src="[https://user-images.githubusercontent.com/58574988/134170370-c827d712-fcc7-432f-b9f8-96678b0c9bf6.gif](https://lh3.googleusercontent.com/fife/AKsag4MpS0hr9WXSGiSgvupnMQys9A7md97sZwElUz96fsy1Sc6mlI0wmHpgxeWQCriNKc2MrF6oEHmq8NjmQJfGgOpn66Air5d3Hz9S5UiuFsIgEJGcbY2pUX1-1AwZR07ZvauOUwy-ix3qM6wpoABrIK9kNcf5Ixoo7BKu7GcMHOmWH6zxpB75By0AUCmTR7w7N6WV03kjv0QHnbt21tmQC8f1owjev_qOBBx0QXMxLe8M6V3MjrkJ6YhV2mZzyZwO8I9tbIkd6C6OuVqhqPQP2cP4B68kdZzuUXu-fmkVdlFXtThjeW371Vr5hyfo3dLaybXStTFq1sWenC3KShsEK6F4WfNLwgjnlH3-EtkpPM_WqpwyZNAe4Wd6VpmjYTSLDqR_9X8GSvGA3yzKBxNRsdNZSCV689rWM2NDed9lB1AGIrbMJX57ope5NNCqATEuajogVHPf90ol2x7ptUPsQn25sGvtw5G57Bu3wZLUGVYw2Z6jobNdJsnk2p2ux_8L5DP7xoj0Bs_F5zCpfX3bUJy9aZW38xVgIfBjDenl8o-xhqrfdPC57tns306NifAylkQplQL6qiKqM8OI-brFXiTbBcOOkXjGvncDbrOnl_W3YyFGl6cGW-kFhBeGpa1uhufTBHf6spP-qguR1rYGeHDaK1afJ4CxfTi2t8bFVa5cMrwFbF_qy0Y9xMXKTg-vpFR_YFjO6QedzUGzXt6lyC240AWdLbTjhIb3fIZDu_e69pKHqAcJn4Yq-UGmwr2a8MUY2y9NSPgDYKr7VgLnjlCmcHsfrkrPQgwFfb6kKWVcY9Usld57O0Wgh7BHTTs8y_OlFf5hCbfCShZbK2CND8PFat6loeyvZUph_Q00DfvaMTGhZltY8BFj8-jnTLF4yAftNGl2IM3z5LG28QCaD5Q8UJRQjEP0_M-TR9IOA-PUYMqzc_uUwzMct5hHog9MW67wIIfMdQYTd47F8WYl-Goy6Xa1jmPlZZwTGPN-2BKATBDvWFOc4W_qXQFnpJZHubmdhQjZgwxA6uQGRPI=w1920-h969)">

   `Ultilities LOL` is an internal skin changer for League of Legends.

</div>

- Change the skin of your champion, your ward, other champions, towers, minions, and jungle monsters in the game.
- Automatic skin database update.
- Support for spectator mode.
- Change skins anytime and unlimited times in a single game.
- Supports all popular languages ​​in the world.
- In-game configuration with <a href="https://github.com/ocornut/imgui">ImGui</a>.
- <a href="https://github.com/nlohmann/json">JSON</a> based configuration saving & loading

# Building
   1. Clone the source with `git clone --recursive https://github.com/R3nzTheCodeGOD/R3nzSkin.git`
   2. Build in Visual Studio 2019/2022 with configuration "Your Region - x64"

# Usage
   1. Compile source or <a href="https://github.com/R3nzTheCodeGOD/R3nzSkin/releases/latest">download</a> a compiled version.
   2. Use `R3nzSkin_Injector.exe` or inject the built DLL into the game yourself.
      - *Administrator* privilege may be needed if the injector failed to inject the DLL.
      - League client can crash if `R3nzSkin` is injected before being in the game.
         - A workaround is to not inject until you are in the game (you will need to be fast to not disrupt the game).
   3. Press <kbd>Insert</kbd> to bring up the menu.
   4. Select the skin for you, your teammates, enemies, and wards.

# Further optimizations
   If your CPU supports AVX / AVX2 / AVX-512 instruction set, you can enable it in project settings. This should result in more performant code, optimized for your CPU. Currently SSE2 instructions are selected in project settings.

# Credits
   This program is an improved and updated version of the <a href="https://github.com/B3akers">B3akers</a>/<a href="https://github.com/B3akers/LeagueSkinChanger">LeagueSkinChanger</a> project.
