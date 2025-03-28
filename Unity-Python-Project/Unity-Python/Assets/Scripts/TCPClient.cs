using System;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using UnityEngine.UIElements;

public class TCPClient : MonoBehaviour
{
    // Fields for the TCP client and network stream
    private TcpClient client;
    private NetworkStream stream;
    private byte[] buffer = new byte[1024]; // Buffer for incoming data

    public GameObject cube;
    void Start()
    {
        try
        {
            // Attempt to connect to the Python server
            client = new TcpClient("127.0.0.1", 5005);  // Server address and port
            stream = client.GetStream();  // Get the network stream for communication
            Debug.Log("Connected to Python server!");

            // Schedule periodic checks for incoming data
            InvokeRepeating(nameof(ReadData), 0f, 0.1f); // Check every 0.1 seconds
        }
        catch (Exception e)
        {
            // Log any connection errors
            Debug.LogError("Connection error: " + e.Message);
        }
    }

    public void ReadData()
    {

        // Check if there is data available to read
        if (stream.DataAvailable)
        {
            // Read data from the stream into the buffer
            int bytesRead = stream.Read(buffer, 0, buffer.Length);

            // Convert the received bytes into a string
            string message = Encoding.UTF8.GetString(buffer, 0, bytesRead).Trim();
            string[] values = message.Split(" ");        
            Vector3 position = new Vector3(0, -Int32.Parse(values[1])/100.0f, Int32.Parse(values[0])/100.0f);

            cube.transform.position = position;
            //Debug.Log("Received message: " + message);
        }
        
    }

    void OnApplicationQuit()
    {
        // Clean up resources when the application quits
        stream?.Close();  // Close the network stream
        client?.Close();  // Close the TCP client
    }


}