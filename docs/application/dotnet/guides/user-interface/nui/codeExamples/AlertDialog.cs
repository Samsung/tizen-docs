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
				btn.Clicked += onBtnClicked;
			}

        private void onBtnClicked(object sender, ClickedEventArgs e)
        {
            var button = new Button()
            {
                Text = "OK",
            };

            button.Clicked += (object s, ClickedEventArgs a) =>
            {
                Navigator?.Pop();
            };

            DialogPage.ShowAlertDialog("Title", "Message", button);
        }
    }

