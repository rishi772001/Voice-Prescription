# Voice-Prescription
Built a GUI application using Tkinter that helps Doctors to prepare prescriptions more efficiently. This uses speech to text conversion and text extraction to prepare prescriptions in the correct format. This project is submitted for Smart India Hackathon 2020. 

With the increasing number of patients, it is very difficult for the doctors to write prescriptions manually and have an account of all the patients. The proposed system will provide a platform for the doctors to dictate their prescription orally instead of typing or writing it manually which saves a lot of time for doctors as well as the patients and avoids human errors to a greater extent .The proposed system converts the voice to text first and then generate prescriptions automatically by extracting the keywords and provides the prescription in the desired format automatically. This system can also generate prescriptions efficiently with just the audio fileof the conversation between the doctor and the patient through a phone call. The patient need not visit the doctor manually for curing very small health issues. It also provides a way to send the prescription through mail personally to the patient so that they need not meet the doctor again for prescription. This system also provides an option for the doctor to sign the prescription after reviewing it. Since the prescription provided is verified by the doctor there is no possibility of mistakes in this system and the security of the patients medical records is maintained.

## Steps:
  1.Import voice or audio file<br>
  2.Converts audio to text<br>
  3.Extracts keywords and prepares prescription in correct format<br>
  4.Displays it for verification and correction if any<br>
  5.Send prescription to patient E-mail in read-only format.<br>
 
## Software Requirements:
  1.[Python 3](https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe)<br>
  2.Ms Word<br>
 
 ## Dependencies:  
  1.python docx - `pip install python-docx`<br>
  2.Speech Recognition - `pip install SpeechRecognition`<br>
  3.PyAudio - `pip install PyAudio`<br>
  4.Model - `pip install https://med7.s3.eu-west-2.amazonaws.com/en_core_med7_lg.tar.gz`  
  5.Nltk - `pip install nltk`  
  6.Spacy - `pip install spacy==2.3.5`  
  7.NameParser - `pip install nameparser`
  
 
 

