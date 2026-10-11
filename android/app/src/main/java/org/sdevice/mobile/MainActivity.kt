package org.sdevice.mobile

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.LinearLayout
import android.widget.TextView

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            setPadding(28, 28, 28, 28)
            setBackgroundColor(Color.rgb(7, 17, 31))
        }
        fun label(text: String, size: Float, color: Int) {
            root.addView(TextView(this).apply {
                this.text = text
                textSize = size
                setTextColor(color)
                gravity = Gravity.CENTER
                setPadding(4, 18, 4, 18)
            })
        }
        label("S DEVICE", 36f, Color.rgb(48, 211, 247))
        label("OS Experience 0.1 • Android Foundation", 16f, Color.WHITE)
        label("AI  |  VISION  |  SERVICES  |  DEVICES", 17f, Color.rgb(149, 210, 237))
        label("Private services: not connected yet", 13f, Color.LTGRAY)
        label("Prototype dashboard — build and verify before device deployment", 12f, Color.GRAY)
        setContentView(root)
    }
}
