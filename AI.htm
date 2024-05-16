<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Generator with TensorFlow Hub</title>
    <style>
        #canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <button id="generate">Generate Image</button>
    <canvas id="canvas"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest"></script>
    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        // Replace with the URL of your desired model from TensorFlow Hub
        const modelUrl = 'https://tfhub.dev/deepmind/biggan-deep-128/1';

        async function generateImage() {
          // Load the pre-trained model from TensorFlow Hub
          const model = await tf.hub.load(modelUrl);

          // Generate random noise as input (adjust for your model)
          const noise = tf.randomNormal([1, 128]);  // Adjust size based on model input

          // Predict the image from noise
          const prediction = model(noise);

          // Reshape and convert the tensor to image data
          const imageData = await prediction.reshape([model.outputs[0].shape[1], model.outputs[0].shape[2], 3]).data();

          // Draw the image on the canvas
          const image = new ImageData(new Uint8ClampedArray(imageData), model.outputs[0].shape[1], model.outputs[0].shape[2]);
          ctx.putImageData(image, 0, 0);
        }

        document.getElementById('generate').addEventListener('click', generateImage);

        // Load TensorFlow.js library
        (async () => {
          await tf.ready();
        })();
    </script>
</body>
</html>
