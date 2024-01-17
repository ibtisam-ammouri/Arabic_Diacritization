# Arabic Diacritization
This is an ongoing project of building a model that predicts diacritics for Arabic texts.

## Experiment 1: 
  ### Goal: 
  Given a sentence like 'هذه الجملة', the model predicts ['1614 1616 1616' , '1618 1615 1618 1614'],  which are the decimal unicode codepoints representing ['  َ  ِ  ِ ' , '  ْ  ُ  ْ  َ '].

  ### Data:
  20000 sentences from the MSA section of the Tashkeela Corpus.
  T. Zerrouki, A. Balla, Tashkeela: Novel corpus of Arabic vocalized texts, data for auto-diacritization systems, Data in Brief (2017), [http://dx.doi.org/10.1016/j.dib.2017.01.011](https://www.sciencedirect.com/science/article/pii/S2352340917300112?via%3Dihub) 

  ### Architecture:
  - Seq-to-Seq word-based model. 
  - Embedding Dimension: 128.
  - One Bidirectional LSTM layer (units=64).
  - Dense Layer (softmax).
  - Ran on high RAM CPU on Google Colab.   
  
  ### Files:
  1. **word-based-model-20000.ipynb**: Main notebook. Make sure to specify the path to your local copy in the second cell.
  2. **Bin_Data**: Pickled lists of input and output sentences.
  3. **half-model.h5**: trained model that can be loaded in (1) instead of running the training loop.
  4. **delete-letters-from-list.py**: A preprocessing step that turned out to be problematic in hindsight.
  5. **word-based-20k-sample-results.PDF**: Some of the model's results printed as a table per each sentence with initial impressions.

  ### Results:
  - Best epoch: Training Loss: 0.0201, Validation Loss: 0.0908, Validation Accuracy: 0.9876
  - Test Loss: 0.0966, Test Accuracy: 0.9881
  - Results seem suspiciously good, but the sampled predictions seem to actually corroborate the results. Most words are correct but see major issue below. 
  - Interesting cases:
      - words that need to be disambiguated in context, e.g. "ان" can be "an", "in", "anna" or "inna" depending on the vowels. The sampled cases show correct disambiguation.
      - words that are skipped. Especially if they are skipped sometimes but not always. Based on the samples, unusual length seems to play a role (2 letters, more than 6).   
  
  ### Issues: 
  - After inspecting the results, I realized that there is a problem in the way I created the labels.
    In an attempt to reduce processing load, I removed the letters from the targets and kept the harakat only.

    I handeled undiacritized words by replacing them with zeros (to preserve their position in the sentence), but I didn't do the same for individual undiacritized letters in otherwise diacritized words.

    The result is that there is no way to determine with certainty the intended positions of the model's predictions.
    For example, if the model predicts the sequence [damma kasra] for a word like [mhnds], I don't know if the result is incomplete but correct [muh(a)ndis], or incorrect [muhind()s].
    
  - Trying to train the same model using GPU raised the following error:
      > UnknownError: Graph execution error: Detected at node CudnnRNN.

    Online forums suggest it might be a bug in an old version of tensorflow, but it's not the one I was using.
    Another suggestion is to update CUDA, which I couldn't do using Google Colab.

### To Do: 
[ ] Edit the file delete-harakat-from-list so it accounts for the number and positions of the letters and harakat.

[ ] Train model again with the new data. 
  
  
