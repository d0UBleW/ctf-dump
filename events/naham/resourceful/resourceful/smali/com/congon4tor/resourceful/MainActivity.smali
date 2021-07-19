.class public Lcom/congon4tor/resourceful/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 19
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 2

    .line 23
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const p1, 0x7f0a001d

    .line 24
    invoke-virtual {p0, p1}, Lcom/congon4tor/resourceful/MainActivity;->setContentView(I)V

    const p1, 0x7f0700a7

    .line 26
    invoke-virtual {p0, p1}, Lcom/congon4tor/resourceful/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/EditText;

    const v0, 0x7f0700dc

    .line 27
    invoke-virtual {p0, v0}, Lcom/congon4tor/resourceful/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    .line 29
    new-instance v1, Lcom/congon4tor/resourceful/MainActivity$1;

    invoke-direct {v1, p0, p1}, Lcom/congon4tor/resourceful/MainActivity$1;-><init>(Lcom/congon4tor/resourceful/MainActivity;Landroid/widget/EditText;)V

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
.end method
