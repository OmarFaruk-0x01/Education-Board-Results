package com.edu.board.result;

import com.facebook.react.bridge.NativeModule;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;
import java.util.Map;
import android.os.Environment;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;
import java.util.HashMap;
import android.util.Log;
import com.facebook.react.bridge.Promise;
import com.facebook.react.bridge.WritableMap;
import com.facebook.react.bridge.Arguments;

public class PdfHandler extends ReactContextBaseJavaModule {
    PdfHandler(ReactApplicationContext context) {
        super(context);
    }

    private void Print(String msg) {
        Log.d("PdfHandler", msg);
    }

    @ReactMethod
    public void downloadFile(String url, String fileName, Promise promise) {
        WritableMap params = Arguments.createMap();
        try {
            String downDirPath = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOCUMENTS)
                    + "/EDU_RESULT";
            String filePath = downDirPath + '/' + fileName;
            Print("Start Download File Function");
            File downDir = new File(downDirPath);
            Print("before check");
            if (!downDir.exists()) {
                downDir.mkdir();
                Print("Folder created!! -- " + downDir.getAbsolutePath());
            } else {
                Print("Folder exsist");
            }

            File outputFile = new File(filePath);
            if (!outputFile.exists()) {
                outputFile.createNewFile();
                Print("file created!!");
            } else {
                Print("file existes!!");
            }

            URL u = new URL(url);
            URLConnection conn = u.openConnection();
            int contentLength = conn.getContentLength();
            DataInputStream stream = new DataInputStream(u.openStream());
            byte[] buffer = new byte[contentLength];
            stream.readFully(buffer);
            stream.close();
            DataOutputStream fos = new DataOutputStream(new FileOutputStream(downDirPath + '/' + fileName));
            fos.write(buffer);
            fos.flush();
            fos.close();
            Print("File Wrote.");
            params.putString("FilePath", outputFile.getAbsolutePath());
            params.putString("Status", "true");
            promise.resolve(params);
        } catch (FileNotFoundException e) {
            params.putString("Error", e.toString());
            params.putString("Status", "true");
            Print("Error DownladFile: FileNotFoundException " + e.toString());
            promise.reject("500", e.toString(), params);
        } catch (IOException e) {
            Print("Error DownladFile: IOException " + e.toString());
            promise.reject("500", e.toString(), params);
        }
    }

    @Override
    public String getName() {
        return "PdfHandler";
    }
}