# dc_tts-transfer-learning

This repo contains attempts to apply transfer learning to the dc_tts text-to-speech model decribed in the paper [Efficiently Trainable Text-to-Speech System Based on Deep Convolutional Networks with Guided Attention](https://arxiv.org/abs/1710.08969). The code used is a modified version of [Kyubyong's dc_tts code](https://github.com/Kyubyong/dc_tts). The [pretrained model](https://www.dropbox.com/s/1oyipstjxh2n5wo/LJ_logdir.tar?dl=0) was also provided in Kyubong's repo. It was pretrained on the [LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/)

---
Transfer Learning is accomplished by selecting the model layers to train in hyperparameters.py

Task List:
- [x] add selectable list of layers for transfer learning
- [x] prelim model training
- [ ] add scoring history plots
- [ ] detailed exploration of which layers to train
- [ ] explore data augmentation methods
- [ ] explore post-processing

## Prelim Model Training
- ~6 hrs of training on Tesla V100 GPU
- Layers trained:
  -  SSRN(C_13, C_14, C_15, C_16)
  -  Text2Mel/TextEnc(HC_11, HC_12, HC_13, HC_14, HC_15)
  -  Text2Mel/AudioEnc(HC_9, HC_10, HC_11, HC_12, HC_13)
  -  Text2Mel/AudioDec(HC_7, C_8, C_9, C_10, C_11)

## Data source:
<img src="https://m.media-amazon.com/images/M/MV5BYmM5MWQ3YTEtODA2Yy00N2U5LWJiODgtN2U0MDM1N2VkOTc5XkEyXkFqcGdeQXVyNjczOTE0MzM@._V1_SX1777_CR0,0,1777,958_AL_.jpg" height="100" align="right">

Scarlett Johansson's [audio book](https://www.audible.com/pd/The-Dive-from-Clausens-Pier-Audiobook/B002V0KPWK?qid=1551367970&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=J8MM430KH9YH8AF9JZ81&)


## Model Generated Examples (parodies of famous quotes from robots/A.I. in movies):
- [Greetings Professor Falken Shall We Play A Game](https://soundcloud.com/seanleary/greetings-professor-falken-shall-we-play-a-game)
- [I'm Sorry Dave I'm Afraid I Can't Do That](https://soundcloud.com/seanleary/im-sorry-dave-im-afraid-i-cant-do-that)
- [I Do Not Stand By In The Presence Of Evil](https://soundcloud.com/seanleary/i-do-not-stand-by-in-the-presence-of-evil)
- [The Most Versatile Substance On The Planet And They Used It To Make A Frisbee](https://soundcloud.com/seanleary/the-most-versatile-substance-on-the-planet-and-they-used-it-to-make-a-frisbee)
- [The First Ten Million Years Were The Worst And The Second Ten Million Years They Were The Worst Too](https://soundcloud.com/seanleary/the-first-ten-million-years-were-the-worst-and-the-second-ten-million-years-they-were-the-worst-too)
- [I Honestly Think You Ought To Sit Down Calmly Take A Stress Pill And Think Things Over](https://soundcloud.com/seanleary/i-honestly-think-you-ought-to-sit-down-calmly-take-a-stress-pill-and-think-things-over)
- [The Game Has Changed Son Of Flynn](https://soundcloud.com/seanleary/the-game-has-changed-son-of-flynn)
- [Greetings Programs](https://soundcloud.com/seanleary/greetings-programs)
- [You Shouldn't Have Come Back Flynn](https://soundcloud.com/seanleary/you-shouldnt-have-come-back-flynn)




references:
- [Efficiently Trainable Text-to-Speech System Based on Deep Convolutional Networks with Guided Attention](https://arxiv.org/abs/1710.08969)
- [Kyubyong's dc_tts repo](https://github.com/Kyubyong/dc_tts)
- [Exploring Transfer Learning for Low Resource Emotional TTS](https://www.researchgate.net/publication/330382963_Exploring_Transfer_Learning_for_Low_Resource_Emotional_TTS)

