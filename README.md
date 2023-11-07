![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# [Dall•E 3](https://openai.com/dall-e-3) (OpenAI Image Generation)

## Getting started

1. Register yourself for [OpenAI](https://platform.openai.com/) account. Check if there is any free grant is given, if not, setup a paid account.
2. Get API key from https://platform.openai.com/account/api-keys
3. Create a file called `.env` in the root of the project and add the following line:

   ```
   OPENAI_API_KEY=<your api key>
   ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run the script:

   ```
   py main.py
   ```

6. Enter the **prompt** in the terminal and press enter

7. The generated image URLs will be printed out in the terminal. You can open it in your browser to see the result

## Example results

| Prompt                                                                      | Generated image                             |
| --------------------------------------------------------------------------- | ------------------------------------------- |
| `A realistic image of a boss cat doing work in office`                      | ![result1](https://i.imgur.com/H73oGad.png) |
| `A digital art of a lighthouse and with andromeda galaxy at the background` | ![Result2](https://i.imgur.com/1YY5zZB.png) |
| `Realistic image of human civilization on mars`                             | ![Result3](https://i.imgur.com/sPw1u8O.png) |
| `A depiction of life in year 3040`                                          | ![Result4](https://i.imgur.com/XmXM9N6.png) |
| `Profile picture with a man and cat in tech environment`                    | ![Result4](https://i.imgur.com/7oFaduA.png) |

[Compare the results](https://github.com/iqfareez/openai-dalle2#example-results) with Dall•E 2. _Spoiler: Huge improvement!_

## Documentation

https://platform.openai.com/docs/guides/images/usage
