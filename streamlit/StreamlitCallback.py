import streamlit as st
from tensorflow.keras.callbacks import Callback

class StreamlitCallback(Callback):
    def on_train_begin(self, logs=None):
        self.text_area = st.empty()  # Reserve a message slot to write to
        self.text_area.write('Starting training')

    def on_epoch_end(self, epoch, logs=None):
        #self.weight_text.text(f'Epoch {epoch}, loss: {logs["loss"]:.4f}, mean_squared_error: {logs["mean_squared_error"]:.4f}, val_loss: {logs["val_loss"]:.4f}, val_mean_squared_error: {logs["val_mean_squared_error"]:.4f}')
        self.text_area.write(f'Epoch {epoch}, loss: {logs["loss"]:.4f}, mean_squared_error: {logs["mean_squared_error"]:.4f}, val_loss: {logs["val_loss"]:.4f}, val_mean_squared_error: {logs["val_mean_squared_error"]:.4f}')
