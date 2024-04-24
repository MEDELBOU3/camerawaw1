import cv2
import shutil

def take_selfie():
    # تفعيل الكاميرا الأمامية
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("لا يمكن التقاط الصورة!")
            break

        # إضافة إطار للصورة الملتقطة
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        cv2.rectangle(frame, (10, 10), (w-10, h-10), (255, 255, 255), 2)

        # عرض النص على الصورة
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Press SPACE to take selfie', (10, h - 30), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # عرض الصورة على الشاشة
        cv2.imshow('Selfie Camera', frame)

        # انتظار الضغط على "q" للخروج و"space" لالتقاط الصورة
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord(' '):
            # حفظ الصورة على جهاز الكمبيوتر
            images = 'C:/Users/PC/Desktop/selfie.jpg'  # تغيير المسار حسب مكان حفظ الصورة
            cv2.imwrite(images, frame)
            print("تم حفظ الصورة بنجاح!")

            # نسخ الصورة إلى المجلد الحالي
            shutil.copy(images, './selfie.jpg')

            # عرض رسالة بعد حفظ الصورة
            cv2.putText(frame, 'Selfie Saved!', (10, h - 60), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow('Selfie Camera', frame)
            cv2.waitKey(1000)  # عرض الرسالة لمدة ثانية واحدة

            break

    # تحرير الكاميرا وإغلاق النوافذ
    cap.release()
    cv2.destroyAllWindows()

# تشغيل الدالة لالتقاط الصورة
take_selfie()