1. Create a new Django project using the following command:
```bash
django-admin startproject myproject
```
2. Create a new Django app using the following command:
```bash
python manage.py startapp myapp
```
3. Install the required packages for Django REST framework using the following command:
```bash
pip install djangorestframework
```
4. Create a new file called `serializers.py` in your app directory and define your serializers for the models you want to use in your API.
```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

5. Create a new file called `views.py` in your app directory and define your views for the API.

```python
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelList(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

6. Add the following lines to your `urls.py` file to define the URLs for your API views.

```python
from django.urls import path
from .views import MyModelList, MyModelDetail

urlpatterns = [
    path('api/mymodels/', MyModelList.as_view()),
    path('api/mymodels/<int:pk>/', MyModelDetail.as_view()),
]
```
7. Install the required packages for ReactJS using the following command:

```bash
npx create-react-app myapp
```

8. Install the required packages for Bootstrap-React using the following command:

```bash
npm install react-bootstrap bootstrap
```

9. Create a new file called `App.js` in your ReactJS app directory and define your components for the calculator and weather modules.

```javascript
import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

function Calculator() {
  return (
    <div>
      <h1>Calculator</h1>
      {/* Add your calculator component here */}
    </div>
  );
}

function Weather() {
  return (
    <div>
      <h1>Weather</h1>
      {/* Add your weather component here */}
    </div>
  );
}

function App() {
  return (
    <Container>
      <Row>
        <Col>
          <Calculator />
        </Col>
        <Col>
          <Weather />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
```

10. Create a new file called `Upload.js` in your ReactJS app directory and define your component for the file upload page.

```javascript
import React, { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';

function Upload() {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState(null);

  const handleFilesChosen = (event) => {
    setFiles(event.target.files);
  };

  const handleUploadClick = async (event) => {
    event.preventDefault();
    setLoading(true);
    setSuccess(false);
    setError(null);

    const formData = new FormData();
    for (let file of files) {
      formData.append('files', file);
    }

    try {
      const response = await fetch('/api/upload/', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error('Failed to upload files');
      }
      setSuccess(true);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleRetrieveClick = async (event) => {
    event.preventDefault();
    setLoading(true);
    setSuccess(false);
    setError(null);

    try {
      const response = await fetch('/api/files/');
      if (!response.ok) {
        throw new Error('Failed to retrieve files');
      }
      const data = await response.json();
      alert(`Number of files: ${data.length}`);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <h1>Upload Files</h1>
      <Form onSubmit={handleUploadClick}>
        <Form.Group>
          <Form.Label>Select files to upload:</Form.Label>
          <Form.Control type="file" multiple={true} accept=".csv,.doc,.docx,.xls,.xlsx,.ppt,.pptx"