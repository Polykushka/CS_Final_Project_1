from ast import Index
from tkinter import *

class Gui:
    def __init__(self, window) -> None:
        """
        Method used to set up the GUI
        :param window: The window that is used to create the GUI
        """
        self.window = window
        self.attempts = None
        # Frame containing label and entry for name
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student name: ')
        self.input_name = Entry(self.frame_name, width=20)
        self.label_name_error = Label(self.frame_name, text='', fg='red')

        # Frame containing label and entry for the number of attempts
        self.frame_attempts = Frame(self.window)
        self.label_attempts = Label(self.frame_attempts, text='No of attempts: ')
        self.input_attempts = Entry(self.frame_attempts, width=20)
        self.button_attempts = Button(self.frame_attempts, text='ENTER', command=self.show)
        self.label_attempts_error = Label(self.frame_attempts, text='', fg='red')

        # Frame containing label and entry for score 1
        self.frame_score1 = Frame(self.window)
        self.label_score1 = Label(self.frame_score1, text='Score 1: ')
        self.input_score1 = Entry(self.frame_score1, width=20)
        self.label_score1_error = Label(self.frame_score1, text='', fg='red')

        # Frame containing label and entry for score 2
        self.frame_score2 = Frame(self.window)
        self.label_score2 = Label(self.frame_score2, text='Score 2: ')
        self.input_score2 = Entry(self.frame_score2, width=20)
        self.label_score2_error = Label(self.frame_score2, text='', fg='red')

        # Frame containing label and entry for score 3
        self.frame_score3 = Frame(self.window)
        self.label_score3 = Label(self.frame_score3, text='Score 3: ')
        self.input_score3 = Entry(self.frame_score3, width=20)
        self.label_score3_error = Label(self.frame_score3, text='', fg='red')

        # Frame containing label and entry for score 4
        self.frame_score4 = Frame(self.window)
        self.label_score4 = Label(self.frame_score4, text='Score 4: ')
        self.input_score4 = Entry(self.frame_score4, width=20)
        self.label_score4_error = Label(self.frame_score4, text='', fg='red')

        '''
        Frame containing button for submitting scores as well as
        labels for the total and average of the scores.
        
        The label for the total score also lets user know if the information they
        have entered is not valid.
        '''
        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='SUBMIT', command=self.submit)
        self.label_total = Label(self.frame_submit, text='') # Also used for invalid information
        self.label_average = Label(self.frame_submit, text='')
        self.button_clear = Button(self.window, text='CLEAR', command=self.clear)

        # Packs contents of the name, ID, and attempt frames
        self.label_name.pack(side='left', padx=5, pady=5)
        self.input_name.pack(side='left', padx=5, pady=5)
        self.label_name_error.pack(side='left', padx=5,pady=5)
        self.label_attempts.pack(side='left', padx=5, pady=5)
        self.input_attempts.pack(side='left', padx=5, pady=5)
        self.button_attempts.pack(side='left', padx=5, pady=5)
        self.label_attempts_error.pack(side='left', padx=5, pady=5)

        # Packs the contents of the frames for scores 1-4

        self.label_score1.pack(side='left', padx=5, pady=5)
        self.input_score1.pack(side='left', padx=5, pady=5)
        self.label_score1_error.pack(side='left', padx=5, pady=5)
        self.label_score2.pack(side='left', padx=5, pady=5)
        self.input_score2.pack(side='left', padx=5, pady=5)
        self.label_score2_error.pack(side='left', padx=5, pady=5)
        self.label_score3.pack(side='left', padx=5, pady=5)
        self.input_score3.pack(side='left', padx=5, pady=5)
        self.label_score3_error.pack(side='left', padx=5, pady=5)
        self.label_score4.pack(side='left', padx=5, pady=5)
        self.input_score4.pack(side='left', padx=5, pady=5)
        self.label_score4_error.pack(side='left', padx=5, pady=5)


        # Packs contents of the submit frame
        self.button_submit.pack(side='top', padx=5, pady=5)
        self.label_total.pack(side='bottom', padx=5, pady=5)
        self.label_average.pack(side='bottom', padx=5, pady=5)

        # Packs name and attempt frames
        self.frame_name.pack(anchor='w')
        self.frame_attempts.pack(anchor='w')
        self.button_clear.pack(side='bottom', padx=5, pady=5)

    def submit(self) -> None:
        '''
        Sends recorded information to an output file and calculates the final score and average score
        '''
        data_is_valid = True

        # Sets the attempts error label to be void
        self.label_attempts_error.config(text='')

        # Lists containing entries and error labels for each score
        score_entries = [self.input_score1, self.input_score2, self.input_score3, self.input_score4]
        error_labels = [self.label_score1_error, self.label_score2_error, self.label_score3_error, self.label_score4_error]
        scores = []

        # Checks whether if info is entered and if it is valid (between 0-100, not a string, etc.)
        for num in range(self.attempts):
            score = 0
            this_data_is_valid = True
            try:
                score = int(score_entries[num].get())
                if int(score_entries[num].get()) < 0 or int(score_entries[num].get()) > 100:
                    raise IndexError
            except ValueError:
                error_labels[num].config(text='Please enter a valid number')
                data_is_valid = False
                this_data_is_valid = False
            except IndexError:
                error_labels[num].config(text='Please enter a number 0-100')
                data_is_valid = False
                this_data_is_valid = False
            if this_data_is_valid:
                error_labels[num].config(text='')
                scores.append(score)
        average = 0
        highest_score = -1
        if data_is_valid:
            # Finds the highest score and calculates the average
            for score in scores:
                average += score
                if score > highest_score:
                    highest_score = score

            # Writes information to the data.csv file
            with open('data.csv', 'a') as file:
                file.write(f'{self.input_name.get()}, ')
            for num in range(4):
                try:
                    with open('data.csv', 'a') as file:
                        file.write(f'{scores[num]}, ')
                except IndexError:
                    with open('data.csv', 'a') as file:
                        file.write(f'{0}, ')
            with open('data.csv', 'a') as file:
                file.write(f'{round(average / len(scores), 2)}, ')
                file.write(f'{highest_score}\n')
            self.label_average.config(text=f'Average is {round(average / len(scores), 2)}%')
            self.label_total.config(text=f'Your final score is {highest_score}%')
        else:
            # Sets average and final labels to be void
            self.label_average.config(text='')
            self.label_total.config(text='')



    def show(self) -> None:
        '''
        Method used to show score entries and labels
        '''
        # Lists containing all frames, entries, and error labels
        frames = [self.frame_score1, self.frame_score2, self.frame_score3, self.frame_score4]
        score_entries = [self.input_score1, self.input_score2, self.input_score3, self.input_score4]
        error_labels = [self.label_score1_error, self.label_score2_error, self.label_score3_error, self.label_score4_error]
        data_is_valid = True
        name = self.input_name.get()
        # Checks to see that the name entry is not blank
        if name == '':
            self.label_name_error.config(text='Please enter a name')
            data_is_valid = False
        else:
            self.label_name_error.config(text='')
        self.attempts = self.input_attempts.get()
        # Verifies that the no. of attempts entered is between 1 and 4 and is an integer
        try:
            self.attempts = int(self.attempts)
            if self.attempts < 1 or self.attempts > 4:
                raise IndexError
            else:
                self.label_attempts_error.config(text='')
        except ValueError:
            self.label_attempts_error.config(text='Please enter a valid number')
            data_is_valid = False
        except IndexError:
            self.label_attempts_error.config(text='Please enter a number 1-4')
            data_is_valid = False
        # Unpacks unneeded frames, sets error labels to void, and clears all score entries
        for num in range(4):
            frames[num].pack_forget()
            error_labels[num].config(text='')
            score_entries[num].delete(0, END)
        # Set average and total labels to void and unpack submit frame
        self.label_average.config(text='')
        self.label_total.config(text='')
        self.frame_submit.pack_forget()

        # Pack all needed frames if information is valid
        if data_is_valid:
            for num in range(int(self.input_attempts.get())):
                frames[num].pack(anchor='w')
            self.frame_submit.pack()

    def clear(self) -> None:
        '''
        Clears the entire form back to its original state
        '''
        # Clears all entries
        self.input_name.delete(0, END)
        self.input_attempts.delete(0, END)
        self.input_score1.delete(0, END)
        self.input_score2.delete(0, END)
        self.input_score3.delete(0, END)
        self.input_score4.delete(0, END)
        # List containing all frames
        frames = [self.frame_score1, self.frame_score2, self.frame_score3, self.frame_score4, self.frame_submit]
        # Unpacks all frames
        for frame in frames:
            frame.pack_forget()
        # Sets attempts back to nothing
        self.attempts = None
        # Sets average and total labels to void
        self.label_total.config(text='')
        self.label_average.config(text='')

