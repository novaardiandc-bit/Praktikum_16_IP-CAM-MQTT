import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt

mqttbroker ="mqtt-dashboard.com"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(mqttbroker)

kirim ="test"

cap = cv2.VideoCapture(0)

mphand = mp.solutions.hands
hands = mphand.Hands()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Gagal membaca kamera!")
        break

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        client.publish(kirim, "ada tangan")
        print("ada tangan")
    else:
        client.publish(kirim, "tidak ada tangan")
        print("tidak ada tangan")

    cv2.imshow('IP Cam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()