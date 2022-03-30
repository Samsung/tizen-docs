using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
	public partial class XamlPage : ContentPage
	{
        public XamlPage()
        {
            InitializeComponent();
            img.Orientation = new Rotation(new Radian((float)System.Math.PI / 4),
                                     new Vector3(0.0f, 0.0f, 1.0f));
        }

        private void onResourceReady(object sender, ImageView.ResourceReadyEventArgs e)
        {

        }
    }
}
