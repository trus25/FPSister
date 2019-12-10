#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Dec 10, 2019 01:59:56 PM +07  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu {{}} -background #645cf8 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 797x712+607+188
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    entry $top.ent64 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black \
        -justify left 
    vTcl:DefineAlias "$top.ent64" "EntryNama" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent65 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -justify left -selectbackground #c4c4c4 \
        -selectforeground black 
    vTcl:DefineAlias "$top.ent65" "EntryAddr" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab66 \
        -background #645cf8 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 20} -foreground $vTcl(actual_gui_fg) \
        -text Nama 
    vTcl:DefineAlias "$top.lab66" "LblNama" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab67 \
        -activebackground #f9f9f9 -activeforeground black -background #645cf8 \
        -disabledforeground #a3a3a3 -font {-family {Segoe UI} -size 20} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {IP Address} 
    vTcl:DefineAlias "$top.lab67" "LblAddress" vTcl:WidgetProc "Toplevel1" 1
    button $top.but68 \
        -activebackground #51ff51 -activeforeground #ffffff \
        -background #00ff00 -borderwidth 0 -disabledforeground #a3a3a3 \
        -font {-family {UD Digi Kyokasho NP-R} -size 28} -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text GO! 
    vTcl:DefineAlias "$top.but68" "BtnGo" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent64 \
        -in $top -x 260 -y 190 -width 250 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent65 \
        -in $top -x 260 -y 310 -width 250 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 260 -y 150 -width 250 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab67 \
        -in $top -x 260 -y 270 -width 250 -height 40 -anchor nw \
        -bordermode ignore 
    place $top.but68 \
        -in $top -x 310 -y 450 -width 150 -relwidth 0 -height 80 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
