using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;
using System.Linq;

namespace NUIXamlSimpleApp
{

    public partial class XamlPage : View
    {
        private MenuTestMenu menu;
        public XamlPage()
        {
            InitializeComponent();
        }

        private void createMenu()
        {
            menu = new MenuTestMenu();
            menu.Anchor = btn1;
            menu.HorizontalPositionToAnchor = Menu.RelativePosition.Center;
            menu.VerticalPositionToAnchor = Menu.RelativePosition.End;
            menu.Post();
        }

        private void MenuItemClicked(object sender, ClickedEventArgs e)
        {
            menu.Dismiss();
        }

        private void btn_Clicked(object sender, ClickedEventArgs e)
        {
            createMenu();
            menu.Post();
        }

    }
}
