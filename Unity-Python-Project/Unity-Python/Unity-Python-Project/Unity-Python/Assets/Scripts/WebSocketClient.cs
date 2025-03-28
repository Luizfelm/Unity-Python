using UnityEngine;
using NativeWebSocket;

public class WebSocketClient : MonoBehaviour
{
    private WebSocket websocket;

    async void Start()
    {
        websocket = new WebSocket("ws://localhost:8765");

        websocket.OnMessage += (bytes) =>
        {
            // Convert the received bytes to a string
            string message = System.Text.Encoding.UTF8.GetString(bytes);
            Debug.Log("Message from Python: " + message);
        };

        await websocket.Connect();
    }

    void Update()
    {
        #if !UNITY_WEBGL || UNITY_EDITOR
        websocket?.DispatchMessageQueue();
        #endif
    }

    private async void OnApplicationQuit()
    {
        await websocket.Close();
    }
}