<template>
  <div class="container">
    <span className='title'>fives</span>
    <div class="letter-bar">
      <div class='letter' v-for="letter in alphabet" :key="letter" @click="toggleLetter(letter)" :class="{underline: selectedLetters.includes(letter)}">
        {{ letter.toUpperCase() }}
      </div>
    </div>
    <span className='small clickable' @click="populateWords()">reset</span>
    <div class="word-container">
      <div v-if="isLoading" class="loading-message">cooking alphabet soup...</div>
      <span v-else class="word" v-for="(word, index) in words" :key="index">
        <a class="unstyled-link" :href="`https://www.merriam-webster.com/dictionary/${word}`" target="_blank">
        <span v-for="(letter, idx) in word" :key="idx" :class="getLetterClass(idx, index)">
          {{ letter }}
        </span>
        </a>
      </span>
    </div>
    <span className="small">type! (if you can)</span>
  </div>
  <!-- <div class="side-credits">
        5757 five-letter english word from the stanford graphbase.
  </div> -->
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      alphabet: 'abcdefghijklmnopqrstuvwxyz'.split(''),
      selectedLetters: ['a'],
      words: [],
      currentWordIndex: 0,
      currentLetterIndex: 0,
      isLoading: false // Added loading state
    };
  },
  methods: {
    toggleLetter(letter) {
      const index = this.selectedLetters.indexOf(letter);
      if (index > -1) {
        this.selectedLetters.splice(index, 1);
      } else {
        this.selectedLetters.push(letter);
      }
    },
    async getWord() {
      if (this.selectedLetters.length !== 0) {
        const response = await axios.post('https://kestelle.pythonanywhere.com/next_word', {
          letters: this.selectedLetters
        });
        return response.data.word;
      } else {
        return 'fives';
      }
    },
    async populateWords() {
      this.isLoading = true;
      this.words = [];
      for (let i = 0; i < 5; i++) {
        const word = await this.getWord();
        this.words.push(word);
      }
      this.isLoading = false;
    },
    getLetterClass(idx, wordIndex) {
      if (wordIndex < this.currentWordIndex) {
        return 'correct';
      } else if (wordIndex === this.currentWordIndex) {
        if (idx < this.currentLetterIndex) {
          return 'correct';
        } else if (idx === this.currentLetterIndex) {
          return 'current';
        }
      }
      return '';
    },
    async onKeydown(event) {
      const currentWord = this.words[this.currentWordIndex];
      const inputLetter = event.key;

      if (inputLetter === currentWord[this.currentLetterIndex]) {
        this.currentLetterIndex++;

        if (this.currentLetterIndex === currentWord.length) {
          this.currentLetterIndex = 0;
          this.words.shift();

          const newWord = await this.getWord();
          this.words.push(newWord);
        }
      }
    }
  },
  mounted() {
    this.populateWords();
    window.addEventListener('keydown', this.onKeydown);
  },
  beforeUnmount() {
    window.removeEventListener('keydown', this.onKeydown);
  }
};
</script>


<style>
  @import url("https://use.typekit.net/qar6hrg.css");
  .small {
    font-family: "aglet-mono-variable-italic", sans-serif;
    font-style: italic;
    font-variation-settings: "wght" 400;
    color: gray;
  }

  .clickable {
    cursor: pointer;
  }

  .clickable:hover, .letter:hover {
    color:white;
  }

  .letter {
    color: gray;
  }

  .unstyled-link {
  text-decoration: none;
  color: inherit;
  /* Additional reset styles */
  font-weight: normal;
  background: none;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
}
.side-credits {
  position: absolute;
  right: 8svw;
  top: 10svh;
  width: 20svw;
}

.loading-message {
  font-size: 2svh;
}

.title {
  font-family: "aglet-mono-variable", sans-serif;
  font-variation-settings: "wght" 400;
  font-size: 8svh;
  color: white;
  text-align: center;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.letter-bar {
  display: flex;
  flex-direction: row;
  font-size: 2svh;
  color: white;
  cursor: pointer;
}

.underline {
  text-decoration: underline;
  cursor: pointer;
}

.word-container {
  display: flex;
  height: 60svh;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  margin: 5svh;
  margin-bottom: 0svh;
  font-size: 8svh;
  font-family: "aglet-mono-variable", sans-serif;
  font-variation-settings: "wght" 400;
}

.word {
  color: gray;
}

.correct {
  color: white;
}

.current {
  background-color: black;
}
</style>
