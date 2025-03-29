import cv2
import socket

def main():
    # Inicializa a captura de vídeo
    cap = cv2.VideoCapture(0)
    
    # Carrega o classificador pré-treinado para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
     # Define server host and port
    HOST = '127.0.0.1'  # Localhost address
    PORT = 5005         # Port to listen on

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified host and port
    server_socket.bind((HOST, PORT))

    # Start listening for incoming connections
    server_socket.listen()
    print("Waiting for connection...")

    # Accept a connection from a client
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")  # Log the client's address
    
    while True:
        # Captura frame por frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # Converte para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detecta rostos na imagem
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Desenha um retângulo ao redor de cada rosto detectado
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            message = f"{x} {y} {w} {h}"
               
        
        # Send the message to the client, appending a newline character
        conn.sendall((message + "\n").encode())
        
        # Mostra a imagem com as detecções
        cv2.imshow('Detecção de Rosto', frame)
        
        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera a captura e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()
    print("Closing connection.")
    conn.close()  # Close the client connection
    server_socket.close()  # Close the server socket

if __name__ == "__main__":
    main()