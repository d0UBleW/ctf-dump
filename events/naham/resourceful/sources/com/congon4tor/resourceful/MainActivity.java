package com.congon4tor.resourceful;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    /* access modifiers changed from: protected */
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) R.layout.activity_main);
        final EditText editText = (EditText) findViewById(R.id.password);
        ((Button) findViewById(R.id.submit)).setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                if (editText.getText().toString().equals("sUp3R_S3cRe7_P4s5w0Rd")) {
                    MainActivity.this.startActivity(new Intent(MainActivity.this, FlagActivity.class));
                    return;
                }
                Toast.makeText(MainActivity.this.getBaseContext(), "Error: Incorrect password", 1).show();
            }
        });
    }
}
