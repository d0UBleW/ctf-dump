package com.congon4tor.resourceful;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class FlagActivity extends AppCompatActivity {
    /* access modifiers changed from: protected */
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) R.layout.activity_flag);
        ((TextView) findViewById(R.id.flagTV)).setText("flag{".concat(getResources().getString(R.string.md5)).concat("}"));
    }
}
