// firebase-messaging-sw.js (letakkan di root hosting)
importScripts("https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/10.12.2/firebase-messaging.js");

const firebaseConfig = {
  apiKey: "AIzaSyBDIRSY2vBMdGK10kGVcj5JYkPOGTI6oGc",
  authDomain: "smartifus.firebaseapp.com",
  projectId: "smartifus",
  storageBucket: "smartifus.appspot.com",
  messagingSenderId: "307663183811",
  appId: "1:307663183811:web:e6d783e210038da31d6776",
  // databaseURL tidak wajib di sini
};

firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notifTitle = (payload.notification && payload.notification.title) || 'Notifikasi';
  const notifOptions = {
    body: (payload.notification && payload.notification.body) || '',
    icon: '/infus-icon.png' // optional, taruh file icon di root hosting jika mau
  };
  self.registration.showNotification(notifTitle, notifOptions);
});

