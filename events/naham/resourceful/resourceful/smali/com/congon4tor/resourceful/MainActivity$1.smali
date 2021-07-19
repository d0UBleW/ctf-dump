.class Lcom/congon4tor/resourceful/MainActivity$1;
.super Ljava/lang/Object;
.source "MainActivity.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/congon4tor/resourceful/MainActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/congon4tor/resourceful/MainActivity;

.field final synthetic val$password:Landroid/widget/EditText;


# direct methods
.method constructor <init>(Lcom/congon4tor/resourceful/MainActivity;Landroid/widget/EditText;)V
    .locals 0

    .line 29
    iput-object p1, p0, Lcom/congon4tor/resourceful/MainActivity$1;->this$0:Lcom/congon4tor/resourceful/MainActivity;

    iput-object p2, p0, Lcom/congon4tor/resourceful/MainActivity$1;->val$password:Landroid/widget/EditText;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 2

    .line 32
    iget-object p1, p0, Lcom/congon4tor/resourceful/MainActivity$1;->val$password:Landroid/widget/EditText;

    invoke-virtual {p1}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object p1

    const-string v0, "sUp3R_S3cRe7_P4s5w0Rd"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_0

    .line 33
    new-instance p1, Landroid/content/Intent;

    iget-object v0, p0, Lcom/congon4tor/resourceful/MainActivity$1;->this$0:Lcom/congon4tor/resourceful/MainActivity;

    const-class v1, Lcom/congon4tor/resourceful/FlagActivity;

    invoke-direct {p1, v0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 34
    iget-object v0, p0, Lcom/congon4tor/resourceful/MainActivity$1;->this$0:Lcom/congon4tor/resourceful/MainActivity;

    invoke-virtual {v0, p1}, Lcom/congon4tor/resourceful/MainActivity;->startActivity(Landroid/content/Intent;)V

    goto :goto_0

    .line 36
    :cond_0
    iget-object p1, p0, Lcom/congon4tor/resourceful/MainActivity$1;->this$0:Lcom/congon4tor/resourceful/MainActivity;

    invoke-virtual {p1}, Lcom/congon4tor/resourceful/MainActivity;->getBaseContext()Landroid/content/Context;

    move-result-object p1

    const/4 v0, 0x1

    const-string v1, "Error: Incorrect password"

    .line 37
    invoke-static {p1, v1, v0}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/Toast;->show()V

    :goto_0
    return-void
.end method
